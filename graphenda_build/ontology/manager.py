"""Sistema de ontologias da Graphenda Engine.

Carrega, valida e disponibiliza ontologias definidas em YAML.
Cada ontologia define entity types (com levels), relationships e aliases.
"""
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class PropertyConfig:
    type: str
    required: bool = False
    default: str | None = None
    description: str | None = None
    valid_values: list[str] | None = None


@dataclass
class EntityTypeConfig:
    name: str
    level: int
    properties: dict[str, PropertyConfig] = field(default_factory=dict)


@dataclass
class RelationshipTypeConfig:
    name: str
    source: str
    target: str
    cross_level: bool = False
    properties: dict[str, PropertyConfig] = field(default_factory=dict)


@dataclass
class OntologySchema:
    name: str
    version: str
    description: str
    entity_types: dict[str, EntityTypeConfig]
    relationship_types: dict[str, RelationshipTypeConfig]
    aliases: dict[str, str]
    seed_entities: dict | None = None
    hierarchy_relationships: dict[str, dict] = field(default_factory=dict)

    @property
    def entity_type_names(self) -> list[str]:
        return list(self.entity_types.keys())

    @property
    def relationship_type_names(self) -> list[str]:
        return list(self.relationship_types.keys())

    def get_types_by_level(self, level: int) -> list[str]:
        return [name for name, cfg in self.entity_types.items() if cfg.level == level]


class OntologyRegistry:
    """Registro de ontologias carregaveis."""

    def __init__(self, ontologies_dir: Path):
        self.ontologies_dir = ontologies_dir
        self._cache: dict[str, OntologySchema] = {}

    def load(self, ontology_name: str) -> OntologySchema:
        if ontology_name in self._cache:
            return self._cache[ontology_name]

        ont_dir = self.ontologies_dir / ontology_name
        if not ont_dir.exists():
            raise FileNotFoundError(f"Ontologia '{ontology_name}' nao encontrada em {ont_dir}")

        schema = self._load_from_dir(ont_dir)
        errors = self.validate(schema)
        if errors:
            raise ValueError(f"Ontologia '{ontology_name}' invalida: {errors}")

        self._cache[ontology_name] = schema
        return schema

    def _load_from_dir(self, ont_dir: Path) -> OntologySchema:
        # Carregar ontology.yaml
        with open(ont_dir / "ontology.yaml") as f:
            raw = yaml.safe_load(f)

        # Carregar aliases.yaml (opcional)
        aliases = {}
        aliases_path = ont_dir / "aliases.yaml"
        if aliases_path.exists():
            with open(aliases_path) as f:
                aliases_raw = yaml.safe_load(f) or {}
            # Support two formats:
            # 1. Flat: {alias_string: CanonicalName}
            # 2. Nested: {EntityType: {CanonicalName: [alias1, ...]}}
            for key, value in aliases_raw.items():
                if key == "version":
                    continue
                if isinstance(value, str):
                    # Flat format: key is alias, value is canonical
                    aliases[key.lower()] = value
                elif isinstance(value, dict):
                    # Nested format: key is EntityType, value is {canonical: [aliases]}
                    for canonical, alias_list in value.items():
                        if isinstance(alias_list, list):
                            for alias in alias_list:
                                aliases[alias.lower()] = canonical

        # Carregar seed_entities.yaml (opcional)
        seeds = None
        seeds_path = ont_dir / "seed_entities.yaml"
        if seeds_path.exists():
            with open(seeds_path) as f:
                seeds = yaml.safe_load(f)

        # Parsear entity types
        entity_types = {}
        for name, cfg in raw.get("entity_types", {}).items():
            props = {}
            for pname, pcfg in cfg.get("properties", {}).items():
                if isinstance(pcfg, dict):
                    props[pname] = PropertyConfig(
                        type=pcfg.get("type", "string"),
                        required=pcfg.get("required", False),
                        default=pcfg.get("default"),
                        description=pcfg.get("description"),
                        valid_values=pcfg.get("valid_values"),
                    )
                else:
                    props[pname] = PropertyConfig(type=str(pcfg))
            entity_types[name] = EntityTypeConfig(name=name, level=cfg["level"], properties=props)

        # Parsear relationship types
        rel_types = {}
        for name, cfg in raw.get("relationship_types", {}).items():
            source = cfg["source"]
            target = cfg["target"]
            # Suporte a source/target como lista (usar primeiro elemento)
            if isinstance(source, list):
                source = source[0]
            if isinstance(target, list):
                target = target[0]
            rel_types[name] = RelationshipTypeConfig(
                name=name,
                source=source,
                target=target,
                cross_level=cfg.get("cross_level", False),
            )

        # Parsear hierarchy_relationships (opcional)
        hierarchy_rels = raw.get("hierarchy_relationships", {})

        return OntologySchema(
            name=raw["name"],
            version=raw["version"],
            description=raw["description"],
            entity_types=entity_types,
            relationship_types=rel_types,
            aliases=aliases,
            seed_entities=seeds,
            hierarchy_relationships=hierarchy_rels,
        )

    def validate(self, schema: OntologySchema) -> list[str]:
        errors = []
        # Verificar que entity types tem level valido
        for name, et in schema.entity_types.items():
            if et.level < 1 or et.level > 4:
                errors.append(f"Entity type '{name}' tem level invalido: {et.level}")

        # Verificar que relationships referenciam entity types existentes
        for name, rt in schema.relationship_types.items():
            if rt.source not in schema.entity_types:
                errors.append(f"Relationship '{name}' referencia source '{rt.source}' inexistente")
            if rt.target not in schema.entity_types:
                errors.append(f"Relationship '{name}' referencia target '{rt.target}' inexistente")

        return errors

    def list_available(self) -> list[str]:
        return [d.name for d in self.ontologies_dir.iterdir()
                if d.is_dir() and not d.name.startswith("_")]

    def get(self, name: str) -> OntologySchema:
        return self.load(name)
