"""Level Assigner: atribui propriedade level a todos os nodes do Neo4j.

Usa a ontologia para determinar o level de cada entity type
e propaga via Cypher para todos os nodes existentes.
"""
from graphenda_build.hierarchy.hierarchy_config import HierarchyConfig


class LevelAssigner:
    """Atribui level a todos os nodes baseado na ontologia."""

    def __init__(self, ontology, neo4j):
        """
        Args:
            ontology: OntologySchema carregado.
            neo4j: Neo4jConnection ativa.
        """
        self.ontology = ontology
        self.neo4j = neo4j
        self.config = HierarchyConfig.from_ontology(ontology)

    def assign_all(self):
        """Atribui level a todos os nodes baseado no entity type."""
        for type_name, type_config in self.ontology.entity_types.items():
            level = type_config.level
            self.neo4j.run(
                f"MATCH (n:{type_name}) SET n.level = $level",
                {"level": level}
            )

    def create_index(self):
        """Cria index no Neo4j por level para performance."""
        self.neo4j.run(
            "CREATE INDEX level_index IF NOT EXISTS FOR (n) ON (n.level)"
        )

    def verify(self) -> dict:
        """Retorna contagem de nodes por level.

        Returns:
            Dict mapping level -> count. Ex: {1: 150, 2: 30, 3: 8}
        """
        result = self.neo4j.run(
            "MATCH (n) WHERE n.level IS NOT NULL "
            "RETURN n.level AS level, count(n) AS count ORDER BY level"
        )
        return {r["level"]: r["count"] for r in result}

    def find_unassigned(self) -> list:
        """Nodes sem level atribuido.

        Returns:
            Lista de dicts com labels e name dos nodes sem level.
        """
        return self.neo4j.run(
            "MATCH (n) WHERE n.level IS NULL RETURN labels(n) AS labels, n.name AS name"
        )
