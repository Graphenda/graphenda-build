"""Configuracao de hierarquia derivada da ontologia.

Mapeia levels para entity types e define os inter-level mappings.
Derivado automaticamente do OntologySchema carregado.
"""
from dataclasses import dataclass, field


@dataclass
class HierarchyConfig:
    """Configuracao de hierarquia derivada da ontologia."""

    levels: dict[int, list[str]] = field(default_factory=dict)
    # Ex: {1: ["Estimator", "DiagnosticTest"], 2: ["StatisticalConcept"], ...}

    inter_level_mappings: dict[str, tuple[int, int]] = field(default_factory=dict)
    # Ex: {"ABSTRACTS": (2, 1), "GROUPS": (3, 2), "PART_OF": (4, 3)}

    @classmethod
    def from_ontology(cls, ontology) -> "HierarchyConfig":
        """Constroi HierarchyConfig a partir de um OntologySchema.

        Args:
            ontology: OntologySchema carregado da FASE 1.

        Returns:
            HierarchyConfig populado com levels e mappings.
        """
        levels: dict[int, list[str]] = {}
        for type_name, type_config in ontology.entity_types.items():
            level = type_config.level
            if level not in levels:
                levels[level] = []
            levels[level].append(type_name)

        # Derivar inter_level_mappings das relationships cross_level da ontologia
        inter_level_mappings: dict[str, tuple[int, int]] = {}
        for rel_name, rel_config in ontology.relationship_types.items():
            if rel_config.cross_level:
                source_type = rel_config.source
                target_type = rel_config.target
                if source_type in ontology.entity_types and target_type in ontology.entity_types:
                    source_level = ontology.entity_types[source_type].level
                    target_level = ontology.entity_types[target_type].level
                    inter_level_mappings[rel_name] = (source_level, target_level)

        return cls(levels=levels, inter_level_mappings=inter_level_mappings)

    def get_types_for_level(self, level: int) -> list[str]:
        """Retorna entity types para um dado level."""
        return self.levels.get(level, [])

    def validate(self) -> list[str]:
        """Valida a configuracao. Retorna lista de erros."""
        errors = []
        if not self.levels:
            errors.append("Nenhum level definido")
        for level in [1, 2, 3]:
            if level not in self.levels:
                errors.append(f"Level {level} nao tem entity types")
        return errors
