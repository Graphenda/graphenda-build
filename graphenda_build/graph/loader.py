"""Load entities and relationships into Neo4j with MERGE.

Domain-agnostic — works with any ontology.
"""

import logging
from typing import Any

from graphenda_shared.models.core import Entity, Relationship
from graphenda_build.ontology.manager import OntologySchema
from graphenda_shared.graph.connection import Neo4jConnection
from graphenda_build.graph.schema import SchemaBuilder

logger = logging.getLogger(__name__)


class GraphLoader:
    """Loads entities and relationships into Neo4j."""

    def __init__(self, conn: Neo4jConnection, ontology: OntologySchema):
        self.conn = conn
        self.ontology = ontology

    # ------------------------------------------------------------------
    # Entity loading
    # ------------------------------------------------------------------

    @staticmethod
    def _build_entity_query(entity: Entity) -> tuple[str, dict[str, Any]]:
        """Build a MERGE query for an entity."""
        label = entity.type.replace(" ", "_")
        props: dict[str, Any] = {"name": entity.name}
        for key, value in entity.properties.items():
            if isinstance(value, dict):
                continue  # Neo4j doesn't support nested maps
            props[key] = value

        set_clauses = ", ".join(f"n.{k} = ${k}" for k in props if k != "name")
        query = f"MERGE (n:{label} {{name: $name}})"
        if set_clauses:
            query += f" SET {set_clauses}"
        return query, props

    def load_entities(self, entities: list[Entity]) -> int:
        """Load entities into Neo4j. Returns count loaded."""
        count = 0
        for entity in entities:
            query, params = self._build_entity_query(entity)
            try:
                self.conn.run(query, params)
                count += 1
                logger.info("  ENTITY: [%s] %s", entity.type, entity.name)
            except Exception as e:
                logger.error("Failed to load entity %s: %s", entity.name, e)
                raise
        logger.info("Loaded %d entities into Neo4j", count)
        return count

    # ------------------------------------------------------------------
    # Relationship loading
    # ------------------------------------------------------------------

    @staticmethod
    def _build_relationship_query(rel: Relationship) -> tuple[str, dict[str, Any]]:
        """Build a MERGE query for a relationship."""
        params: dict[str, Any] = {
            "source_name": rel.source,
            "target_name": rel.target,
        }
        parts = [
            "MATCH (s {name: $source_name})",
            "MATCH (t {name: $target_name})",
            f"MERGE (s)-[r:{rel.relation}]->(t)",
        ]
        if rel.properties:
            set_parts = []
            for key, value in rel.properties.items():
                param_key = f"rel_{key}"
                params[param_key] = value
                set_parts.append(f"r.{key} = ${param_key}")
            parts.append(f"SET {', '.join(set_parts)}")

        return "\n".join(parts), params

    def load_relationships(self, relationships: list[Relationship]) -> int:
        """Load relationships into Neo4j. Returns count loaded."""
        count = 0
        for rel in relationships:
            query, params = self._build_relationship_query(rel)
            try:
                self.conn.run(query, params)
                count += 1
                logger.info(
                    "  RELATIONSHIP: %s -[%s]-> %s",
                    rel.source, rel.relation, rel.target,
                )
            except Exception as e:
                logger.error(
                    "Failed to load relationship %s -> %s: %s",
                    rel.source, rel.target, e,
                )
                raise
        logger.info("Loaded %d relationships into Neo4j", count)
        return count

    # ------------------------------------------------------------------
    # Seed data
    # ------------------------------------------------------------------

    def _parse_seed_entities(self) -> tuple[list[Entity], list[Relationship]]:
        """Parse seed_entities from ontology into Entity/Relationship lists.

        Seed YAML structure:
          entities:           # flat list, each item has 'name', 'type', 'properties'
            - name: X
              type: EntityType
              properties: {k: v}
          relationships:      # flat list, each item has 'source', 'relation', 'target'
            - source: X
              relation: REL_TYPE
              target: Y
        """
        seeds = self.ontology.seed_entities
        if not seeds:
            return [], []

        entities: list[Entity] = []
        relationships: list[Relationship] = []

        # Parse entities
        for item in seeds.get("entities", []):
            if not isinstance(item, dict):
                continue
            name = item.get("name")
            if not name:
                continue
            entity_type = item.get("type", "Unknown")
            props = item.get("properties", {})
            if not isinstance(props, dict):
                props = {}
            entities.append(Entity(name=name, type=entity_type, properties=props))

        # Parse relationships
        for item in seeds.get("relationships", []):
            if not isinstance(item, dict):
                continue
            source = item.get("source")
            relation = item.get("relation")
            target = item.get("target")
            if not (source and relation and target):
                continue
            nested = item.get("properties")
            if isinstance(nested, dict):
                rel_props = nested
            else:
                rel_props = {k: v for k, v in item.items()
                             if k not in ("source", "relation", "target")}
            relationships.append(Relationship(
                source=source,
                relation=relation,
                target=target,
                properties=rel_props,
            ))

        return entities, relationships

    def load_seed_data(self) -> tuple[int, int]:
        """Load seed entities from ontology into Neo4j.

        Initializes schema first, then loads entities and relationships.
        """
        schema_builder = SchemaBuilder(self.conn, self.ontology)
        schema_builder.initialize()

        entities, relationships = self._parse_seed_entities()
        n_ent = self.load_entities(entities)
        n_rel = self.load_relationships(relationships)

        logger.info("Seed data loaded: %d entities, %d relationships", n_ent, n_rel)
        return n_ent, n_rel
