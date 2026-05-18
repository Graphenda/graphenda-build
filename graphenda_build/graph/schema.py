"""Ontology-driven Neo4j schema builder for Graphenda Engine.

Generates constraints and indexes dynamically from the ontology
instead of hardcoding them per entity type.
"""

import logging
from typing import Any

from graphenda_build.ontology.manager import OntologySchema
from graphenda_shared.graph.connection import Neo4jConnection

logger = logging.getLogger(__name__)


class SchemaBuilder:
    """Generates Neo4j constraints and indexes from an OntologySchema."""

    def __init__(self, conn: Neo4jConnection, ontology: OntologySchema):
        self.conn = conn
        self.ontology = ontology

    def _constraint_queries(self) -> list[str]:
        """Generate uniqueness constraints for every entity type."""
        queries = []
        for entity_name in self.ontology.entity_types:
            safe = entity_name.replace(" ", "_")
            queries.append(
                f"CREATE CONSTRAINT {safe.lower()}_name IF NOT EXISTS "
                f"FOR (n:{safe}) REQUIRE n.name IS UNIQUE"
            )
        return queries

    def _index_queries(self) -> list[str]:
        """Generate indexes per entity type and per level."""
        queries: list[str] = []

        # Index on required string properties for each entity type
        for entity_name, cfg in self.ontology.entity_types.items():
            safe = entity_name.replace(" ", "_")
            for prop_name, prop_cfg in cfg.properties.items():
                if prop_cfg.required and prop_cfg.type == "string" and prop_name != "name":
                    idx_name = f"{safe.lower()}_{prop_name}"
                    queries.append(
                        f"CREATE INDEX {idx_name} IF NOT EXISTS "
                        f"FOR (n:{safe}) ON (n.{prop_name})"
                    )

        # Composite index per level — fulltext search over all types at each level
        for level in range(1, 5):
            types_at_level = self.ontology.get_types_by_level(level)
            if types_at_level:
                label_expr = "|".join(t.replace(" ", "_") for t in types_at_level)
                idx_name = f"level_{level}_search"
                queries.append(
                    f"CREATE FULLTEXT INDEX {idx_name} IF NOT EXISTS "
                    f"FOR (n:{label_expr}) ON EACH [n.name, n.description]"
                )

        return queries

    def initialize(self) -> dict[str, Any]:
        """Create all constraints and indexes. Returns summary."""
        constraints = self._constraint_queries()
        indexes = self._index_queries()

        created_constraints = 0
        for q in constraints:
            try:
                self.conn.run(q)
                created_constraints += 1
                logger.debug("Created: %s", q[:80])
            except Exception as e:
                logger.warning("Constraint may already exist: %s", e)

        created_indexes = 0
        for q in indexes:
            try:
                self.conn.run(q)
                created_indexes += 1
                logger.debug("Created: %s", q[:80])
            except Exception as e:
                logger.warning("Index may already exist: %s", e)

        logger.info(
            "Schema initialized: %d constraints, %d indexes",
            created_constraints, created_indexes,
        )
        return {
            "constraints": created_constraints,
            "indexes": created_indexes,
            "entity_types": len(self.ontology.entity_types),
        }

    def drop_all_data(self) -> None:
        """Drop all nodes and relationships. USE WITH CAUTION."""
        self.conn.run("MATCH (n) DETACH DELETE n")
        logger.warning("All data deleted from Neo4j")
