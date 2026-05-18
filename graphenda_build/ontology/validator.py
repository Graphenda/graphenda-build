"""Valida uma ontologia contra o meta-schema."""
import sys
from pathlib import Path

from graphenda_build.ontology.manager import OntologyRegistry


def main():
    if len(sys.argv) < 2:
        print("Uso: python -m graphenda_build.ontology.validator <ontology_name>")
        sys.exit(1)

    ontology_name = sys.argv[1]
    registry = OntologyRegistry(Path("ontologies"))

    try:
        schema = registry.load(ontology_name)
        print(f"Ontologia '{schema.name}' v{schema.version} carregada com sucesso.")
        print(f"  Entity types: {len(schema.entity_types)}")
        print(f"  Relationship types: {len(schema.relationship_types)}")
        print(f"  Aliases: {len(schema.aliases)}")
        for level in range(1, 5):
            types = schema.get_types_by_level(level)
            if types:
                print(f"  Level {level}: {', '.join(types)}")
    except Exception as e:
        print(f"ERRO: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
