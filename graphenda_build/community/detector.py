"""Community detection using the Leiden algorithm on the knowledge graph."""

import logging
from typing import Any

import igraph as ig
import leidenalg

from graphenda_shared.graph.connection import Neo4jConnection

logger = logging.getLogger(__name__)


class CommunityDetector:
    """Detects communities in the knowledge graph using the Leiden algorithm.

    Exports the Neo4j graph to igraph format, runs community detection,
    and stores the resulting community assignments back in Neo4j.
    """

    def __init__(self, connection: Neo4jConnection, resolution: float = 1.0) -> None:
        self._conn = connection
        self._resolution = resolution

    def detect(self) -> dict[int, list[str]]:
        """Run community detection on the full knowledge graph.

        Returns:
            Dictionary mapping community_id to list of entity names.
        """
        logger.info("Starting community detection with resolution=%.2f", self._resolution)

        graph = self._export_graph()
        if graph.vcount() == 0:
            logger.warning("Empty graph — no communities to detect")
            return {}

        logger.info("Exported graph: %d nodes, %d edges", graph.vcount(), graph.ecount())

        partitions = self._run_leiden(graph)
        communities = self._partition_to_dict(graph, partitions)

        logger.info("Detected %d communities", len(communities))
        self._store_communities(communities)

        return communities

    def _export_graph(self) -> ig.Graph:
        """Export Neo4j knowledge graph to igraph (undirected)."""
        node_records = self._conn.run(
            "MATCH (n) WHERE n.name IS NOT NULL "
            "AND NOT 'Chunk' IN labels(n) "
            "AND NOT '_PipelineMeta' IN labels(n) "
            "RETURN id(n) AS neo4j_id, n.name AS name, labels(n) AS labels"
        )

        nodes = []
        neo4j_to_idx: dict[int, int] = {}
        for rec in node_records:
            idx = len(nodes)
            neo4j_to_idx[rec["neo4j_id"]] = idx
            nodes.append({"name": rec["name"], "labels": rec["labels"]})

        edge_records = self._conn.run(
            "MATCH (a)-[r]->(b) "
            "WHERE a.name IS NOT NULL AND b.name IS NOT NULL "
            "AND NOT 'Chunk' IN labels(a) AND NOT 'Chunk' IN labels(b) "
            "AND NOT '_PipelineMeta' IN labels(a) AND NOT '_PipelineMeta' IN labels(b) "
            "RETURN id(a) AS source_id, id(b) AS target_id, type(r) AS rel_type"
        )

        edges = []
        edge_attrs: list[str] = []
        for rec in edge_records:
            src = neo4j_to_idx.get(rec["source_id"])
            tgt = neo4j_to_idx.get(rec["target_id"])
            if src is not None and tgt is not None:
                edges.append((src, tgt))
                edge_attrs.append(rec["rel_type"])

        graph = ig.Graph(n=len(nodes), edges=edges, directed=False)
        graph.vs["name"] = [n["name"] for n in nodes]
        graph.vs["labels"] = [n["labels"] for n in nodes]
        graph.es["rel_type"] = edge_attrs
        graph.simplify(combine_edges="first")

        return graph

    def _run_leiden(self, graph: ig.Graph) -> leidenalg.VertexPartition:
        partition = leidenalg.find_partition(
            graph,
            leidenalg.RBConfigurationVertexPartition,
            resolution_parameter=self._resolution,
            seed=42,
        )
        logger.info(
            "Leiden complete: %d communities, modularity=%.4f",
            len(partition), partition.modularity,
        )
        return partition

    def _partition_to_dict(
        self, graph: ig.Graph, partition: leidenalg.VertexPartition
    ) -> dict[int, list[str]]:
        communities: dict[int, list[str]] = {}
        for cid, members in enumerate(partition):
            names = [graph.vs[idx]["name"] for idx in members]
            if names:
                communities[cid] = sorted(names)
        return communities

    def _store_communities(self, communities: dict[int, list[str]]) -> None:
        self._conn.run("MATCH (n) WHERE n.community_id IS NOT NULL REMOVE n.community_id")
        for cid, members in communities.items():
            for name in members:
                self._conn.run(
                    "MATCH (n) WHERE n.name = $name SET n.community_id = $community_id",
                    {"name": name, "community_id": cid},
                )
        logger.info("Stored community assignments for %d communities", len(communities))

    def get_community_members(self, community_id: int) -> list[dict]:
        return self._conn.run(
            "MATCH (n) WHERE n.community_id = $community_id "
            "RETURN n.name AS name, labels(n) AS labels, n.description AS description",
            {"community_id": community_id},
        )

    def get_stats(self) -> dict[str, Any]:
        records = self._conn.run(
            "MATCH (n) WHERE n.community_id IS NOT NULL "
            "RETURN n.community_id AS cid, count(n) AS size ORDER BY size DESC"
        )
        sizes = {r["cid"]: r["size"] for r in records}
        unassigned_records = self._conn.run(
            "MATCH (n) WHERE n.community_id IS NULL AND n.name IS NOT NULL "
            "RETURN count(n) AS count"
        )
        unassigned = unassigned_records[0]["count"] if unassigned_records else 0
        s = list(sizes.values())
        return {
            "num_communities": len(sizes),
            "community_sizes": sizes,
            "total_assigned_nodes": sum(s),
            "unassigned_nodes": unassigned,
            "avg_community_size": sum(s) / len(s) if s else 0,
            "min_community_size": min(s) if s else 0,
            "max_community_size": max(s) if s else 0,
        }
