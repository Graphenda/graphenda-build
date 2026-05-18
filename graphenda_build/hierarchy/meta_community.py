"""Meta-Community Builder: cria Knowledge Systems (Level 4).

Agrupa comunidades existentes (Level 3) em meta-comunidades
usando Leiden algorithm sobre embeddings de community summaries.
"""
import logging

import numpy as np

logger = logging.getLogger(__name__)

# Dimensao dos embeddings (compativel com modelo usado no projeto)
EMBEDDING_DIMENSION = 1536

# Cypher para criar vector index dos KnowledgeSystem embeddings
CREATE_VECTOR_INDEX_CYPHER = """
CALL db.index.vector.createNodeIndex(
    'system_embeddings',
    'KnowledgeSystem',
    'embedding',
    {dimension},
    'cosine'
)
""".strip()


class MetaCommunityBuilder:
    """Constroi meta-communities (Level 4) a partir de communities (Level 3)."""

    def __init__(self, neo4j, summarizer):
        """
        Args:
            neo4j: Neo4jConnection ativa.
            summarizer: CommunitySummarizer para gerar summaries das meta-communities.
        """
        self.neo4j = neo4j
        self.summarizer = summarizer

    def build(self, resolution: float = 0.5):
        """Constroi meta-communities completas.

        Args:
            resolution: Parametro Leiden. Baixo = menos clusters maiores.

        Steps:
            1. Exporta community summaries como nodes de um grafo secundario
            2. Calcula similaridade entre community embeddings
            3. Roda Leiden com resolution baixa -> meta-communities
            4. Cria KnowledgeSystem nodes (Level 4)
            5. Cria relacoes PART_OF (L4->L3)
            6. Gera summaries das meta-communities
        """
        # Step 1: Exportar communities existentes
        communities = self._get_communities()
        if not communities:
            logger.warning("Nenhuma community L3 com summary encontrada")
            return

        logger.info("Encontradas %d communities L3 para agrupar", len(communities))

        # Fallback: se poucas communities, criar um unico KnowledgeSystem
        if len(communities) < 3:
            logger.warning(
                "Poucas communities (%d < 3), criando KnowledgeSystem unico",
                len(communities),
            )
            meta_assignments = {0: [c["name"] for c in communities]}
        else:
            # Step 2: Construir grafo de similaridade entre communities
            similarity_graph = self._build_similarity_graph(communities)

            # Step 3: Leiden com resolution baixa
            meta_assignments = self._detect_meta_communities(
                similarity_graph, resolution=resolution
            )

        logger.info(
            "Meta-communities detectadas: %d", len(meta_assignments)
        )

        # Step 4: Criar KnowledgeSystem nodes
        for meta_id, member_communities in meta_assignments.items():
            system_name = f"KnowledgeSystem_{meta_id}"
            self._create_system_node(system_name, member_communities)

        # Step 5: Criar relacoes PART_OF
        self._link_systems_to_domains(meta_assignments)

        # Step 6: Summarizar meta-communities
        self._summarize_systems(meta_assignments)

        # Step 7: Criar vector index
        self._create_vector_index()

    def _get_communities(self) -> list[dict]:
        """Exporta communities existentes com seus summaries e embeddings.

        Returns:
            Lista de dicts com name, summary, embedding de cada community.
        """
        return self.neo4j.run("""
            MATCH (c)
            WHERE c.level = 3 AND c.summary IS NOT NULL
            RETURN c.name AS name, c.summary AS summary,
                   c.embedding AS embedding
        """)

    def _build_similarity_graph(self, communities: list[dict]) -> dict:
        """Constroi grafo onde nodes sao communities e edges sao
        similaridade cosine entre embeddings dos summaries.

        Args:
            communities: Lista de communities com embeddings.

        Returns:
            Dict com nodes e edges (adjacency list).
        """
        nodes = [c["name"] for c in communities]
        embeddings = {c["name"]: np.array(c["embedding"]) for c in communities}
        edges = []

        for i, name_a in enumerate(nodes):
            for name_b in nodes[i + 1:]:
                emb_a = embeddings[name_a]
                emb_b = embeddings[name_b]
                norm_a = np.linalg.norm(emb_a)
                norm_b = np.linalg.norm(emb_b)
                if norm_a == 0 or norm_b == 0:
                    continue
                similarity = float(
                    np.dot(emb_a, emb_b) / (norm_a * norm_b)
                )
                if similarity > 0.3:  # threshold minimo
                    edges.append((name_a, name_b, similarity))

        return {"nodes": nodes, "edges": edges}

    def _detect_meta_communities(
        self, graph: dict, resolution: float
    ) -> dict[int, list[str]]:
        """Leiden algorithm com resolution baixa (menos, maiores clusters).

        Args:
            graph: Grafo de similaridade entre communities.
            resolution: Parametro Leiden.

        Returns:
            Dict mapping meta_community_id -> lista de community names.
        """
        import igraph as ig
        import leidenalg

        g = ig.Graph()
        g.add_vertices(graph["nodes"])
        edge_list = [(e[0], e[1]) for e in graph["edges"]]
        weights = [e[2] for e in graph["edges"]]
        g.add_edges(edge_list)
        g.es["weight"] = weights

        partition = leidenalg.find_partition(
            g, leidenalg.RBConfigurationVertexPartition,
            weights="weight", resolution_parameter=resolution,
        )

        assignments: dict[int, list[str]] = {}
        for idx, community_id in enumerate(partition.membership):
            if community_id not in assignments:
                assignments[community_id] = []
            assignments[community_id].append(graph["nodes"][idx])

        return assignments

    def _create_system_node(self, system_name: str, member_communities: list[str]):
        """Cria node KnowledgeSystem (Level 4) no Neo4j.

        Args:
            system_name: Nome do KnowledgeSystem.
            member_communities: Lista de community names membros.
        """
        self.neo4j.run("""
            MERGE (ks:KnowledgeSystem {name: $name})
            SET ks.level = 4,
                ks.member_count = $count
        """, {"name": system_name, "count": len(member_communities)})

    def _link_systems_to_domains(self, meta_assignments: dict[int, list[str]]):
        """Cria relacoes PART_OF entre KnowledgeSystem (L4) e domains (L3).

        Args:
            meta_assignments: Mapping meta_id -> lista de community names.
        """
        for meta_id, members in meta_assignments.items():
            system_name = f"KnowledgeSystem_{meta_id}"
            for member_name in members:
                self.neo4j.run("""
                    MATCH (ks:KnowledgeSystem {name: $system})
                    MATCH (domain {name: $domain, level: 3})
                    MERGE (ks)-[:PART_OF]->(domain)
                """, {"system": system_name, "domain": member_name})

    def _summarize_systems(self, meta_assignments: dict[int, list[str]]):
        """Gera summaries e embeddings para cada KnowledgeSystem.

        Args:
            meta_assignments: Mapping meta_id -> lista de community names.
        """
        for meta_id, members in meta_assignments.items():
            system_name = f"KnowledgeSystem_{meta_id}"

            # Coletar summaries dos membros
            member_summaries = self.neo4j.run("""
                MATCH (domain)
                WHERE domain.name IN $members AND domain.level = 3
                RETURN domain.summary AS summary
            """, {"members": members})

            combined_text = "\n".join(
                r["summary"] for r in member_summaries if r["summary"]
            )

            # Gerar summary via LLM
            summary = self.summarizer.summarize(
                combined_text,
                context=f"Knowledge System containing: {', '.join(members)}",
            )

            # Gerar embedding do summary
            embedding = self.summarizer.embed(summary)

            # Salvar no Neo4j
            self.neo4j.run("""
                MATCH (ks:KnowledgeSystem {name: $name})
                SET ks.summary = $summary, ks.embedding = $embedding
            """, {"name": system_name, "summary": summary, "embedding": embedding})

            logger.info("KnowledgeSystem %s: summary gerado", system_name)

    def _create_vector_index(self):
        """Cria vector index para embeddings dos KnowledgeSystem nodes."""
        try:
            self.neo4j.run(
                CREATE_VECTOR_INDEX_CYPHER.format(dimension=EMBEDDING_DIMENSION)
            )
            logger.info("Vector index 'system_embeddings' criado")
        except Exception as e:
            # Index pode ja existir
            if "already exists" in str(e).lower():
                logger.info("Vector index 'system_embeddings' ja existe")
            else:
                logger.warning("Falha ao criar vector index: %s", e)

    def verify(self) -> dict:
        """Verifica meta-communities criadas.

        Returns:
            Dict com estatisticas: system_count, part_of_count, traversal_ok.
        """
        systems = self.neo4j.run(
            "MATCH (ks:KnowledgeSystem) RETURN count(ks) AS count"
        )
        part_of = self.neo4j.run(
            "MATCH ()-[r:PART_OF]->() RETURN count(r) AS count"
        )
        traversal = self.neo4j.run("""
            MATCH (l4:KnowledgeSystem)-[:PART_OF]->(l3)-[:GROUPS]->(l2)-[:ABSTRACTS]->(l1)
            WHERE l4.level = 4 AND l3.level = 3 AND l2.level = 2 AND l1.level = 1
            RETURN count(*) AS paths
        """)
        return {
            "system_count": systems[0]["count"] if systems else 0,
            "part_of_count": part_of[0]["count"] if part_of else 0,
            "full_traversal_paths": traversal[0]["paths"] if traversal else 0,
        }
