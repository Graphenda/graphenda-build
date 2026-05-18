"""Entity Resolver ontology-aware.

Resolve nomes de entidades para formas canonicas usando aliases
da ontologia ativa. Suporta match exato, case-insensitive e fuzzy.
"""
import logging
from dataclasses import dataclass
from difflib import SequenceMatcher

from graphenda_build.ontology.manager import OntologySchema

logger = logging.getLogger(__name__)


@dataclass
class ResolvedTriple:
    """Triple com entidades resolvidas para formas canonicas."""

    subject: str
    predicate: str
    object: str
    subject_type: str = ""
    object_type: str = ""
    source_chunk_id: str = ""
    confidence: float = 1.0

    def key(self) -> tuple[str, str, str]:
        return (self.subject, self.predicate, self.object)


class EntityResolver:
    """Resolve entidades usando aliases da ontologia ativa.

    Carrega aliases do OntologySchema e aplica:
    1. Match exato (case-sensitive)
    2. Match case-insensitive
    3. Fuzzy matching (threshold configuravel)
    """

    def __init__(
        self,
        ontology: OntologySchema,
        fuzzy_threshold: int = 85,
    ) -> None:
        self._ontology = ontology
        self._fuzzy_threshold = fuzzy_threshold
        self._valid_entity_types = set(ontology.entity_type_names)

        # Alias maps construidos da ontologia
        # ontology.aliases = {alias_lower: canonical_name}
        self._aliases_lower: dict[str, str] = dict(ontology.aliases)
        # Construir mapa case-sensitive a partir do aliases YAML original
        self._aliases_exact: dict[str, str] = {}
        self._canonicals: set[str] = set()
        self._canonical_types: dict[str, str] = {}

        self._build_alias_maps()

        self._stats = {
            "resolved_exact": 0,
            "resolved_fuzzy": 0,
            "unresolved": 0,
            "duplicates_merged": 0,
        }
        self._unresolved: list[str] = []

    def _build_alias_maps(self) -> None:
        """Constroi mapas de aliases a partir da ontologia."""
        # Canonicals sao os alias targets
        for canonical in self._aliases_lower.values():
            self._canonicals.add(canonical)

        # Reconstruir canonical -> entity_type a partir do aliases YAML
        # O OntologyRegistry carrega aliases_raw mas so guarda {alias_lower: canonical}
        # Precisamos recarregar para obter o entity type de cada canonical
        self._infer_canonical_types_from_aliases()

        # Extrair entity types dos seed_entities
        if self._ontology.seed_entities:
            entities_list = self._ontology.seed_entities.get("entities", [])
            if isinstance(entities_list, list):
                for entity in entities_list:
                    if isinstance(entity, dict):
                        name = entity.get("name", "")
                        etype = entity.get("type", "")
                        if name:
                            self._canonicals.add(name)
                            if etype:
                                self._canonical_types[name] = etype

        # Aliases: lower -> canonical ja esta no self._aliases_lower
        # Tambem popular exact (preservar case do canonical)
        for alias_lower, canonical in self._aliases_lower.items():
            self._aliases_exact[alias_lower] = canonical

    def _infer_canonical_types_from_aliases(self) -> None:
        """Infere canonical -> entity_type invertendo o alias map.

        No aliases YAML, a estrutura e:
            EntityType:
              CanonicalName: [alias1, alias2, ...]

        Inverte para: CanonicalName -> EntityType
        """
        # Agrupar aliases por canonical e verificar quais entity types existem
        # Usar os entity_type_names da ontologia como chave
        for canonical in self._canonicals:
            # Tentar encontrar qual entity type contem este canonical
            # Heuristica: se o canonical name esta no aliases como target,
            # podemos verificar se algum entity type bate
            pass

        # Abordagem direta: recarregar aliases.yaml se disponivel
        try:
            import yaml
            from pathlib import Path

            # Procurar aliases.yaml no diretorio de ontologias
            # O nome da ontologia esta no schema
            possible_paths = [
                Path("ontologies") / self._ontology.name.lower().replace(" ", "_") / "aliases.yaml",
                Path("ontologies") / "model_intelligence" / "aliases.yaml",
            ]

            for aliases_path in possible_paths:
                if aliases_path.exists():
                    with open(aliases_path, encoding="utf-8") as f:
                        aliases_raw = yaml.safe_load(f) or {}

                    for entity_type, names in aliases_raw.items():
                        if entity_type == "version":
                            continue
                        if isinstance(names, dict):
                            for canonical_name in names:
                                self._canonical_types[canonical_name] = entity_type
                                self._canonicals.add(canonical_name)
                    break
        except Exception as e:
            logger.debug("Nao foi possivel recarregar aliases.yaml: %s", e)

        logger.info(
            "EntityResolver: %d aliases, %d canonicals da ontologia '%s'",
            len(self._aliases_lower),
            len(self._canonicals),
            self._ontology.name,
        )

    def resolve_entity(self, name: str, entity_type: str = "") -> tuple[str, str]:
        """Resolve nome de entidade para forma canonica.

        Args:
            name: Nome da entidade.
            entity_type: Tipo hint opcional.

        Returns:
            Tupla (canonical_name, canonical_type).
        """
        if not name or not name.strip():
            return name, entity_type

        name = name.strip()

        # 1. Ja e canonical?
        if name in self._canonicals:
            resolved_type = self._canonical_types.get(name, entity_type)
            self._stats["resolved_exact"] += 1
            return name, resolved_type

        # 2. Match exato (case-insensitive)
        lower = name.lower()
        if lower in self._aliases_lower:
            canonical = self._aliases_lower[lower]
            resolved_type = self._canonical_types.get(canonical, entity_type)
            self._stats["resolved_exact"] += 1
            logger.debug("Match exato: '%s' -> '%s'", name, canonical)
            return canonical, resolved_type

        # 3. Fuzzy match
        fuzzy = self._fuzzy_match(name)
        if fuzzy is not None:
            resolved_type = self._canonical_types.get(fuzzy, entity_type)
            self._stats["resolved_fuzzy"] += 1
            logger.info("Fuzzy match: '%s' -> '%s'", name, fuzzy)
            return fuzzy, resolved_type

        # 4. Nao resolvido
        self._stats["unresolved"] += 1
        self._unresolved.append(name)
        logger.warning("Entidade nao resolvida: '%s' (type='%s')", name, entity_type)
        return name, entity_type

    def resolve_triples(self, triples: list[ResolvedTriple]) -> list[ResolvedTriple]:
        """Resolve entidades em lista de triples e deduplica.

        Args:
            triples: Triples com nomes brutos.

        Returns:
            Triples com nomes canonicos, deduplicados.
        """
        resolved: list[ResolvedTriple] = []
        for triple in triples:
            canonical_subject, subject_type = self.resolve_entity(
                triple.subject, triple.subject_type
            )
            canonical_object, object_type = self.resolve_entity(
                triple.object, triple.object_type
            )

            resolved.append(ResolvedTriple(
                subject=canonical_subject,
                predicate=triple.predicate,
                object=canonical_object,
                subject_type=subject_type,
                object_type=object_type,
                source_chunk_id=triple.source_chunk_id,
                confidence=triple.confidence,
            ))

        return self._deduplicate(resolved)

    def _fuzzy_match(self, name: str) -> str | None:
        best_match = None
        best_score = 0.0
        name_lower = name.lower()

        for canonical in self._canonicals:
            score = SequenceMatcher(None, name_lower, canonical.lower()).ratio() * 100
            if score > best_score:
                best_score = score
                best_match = canonical

        for alias, canonical in self._aliases_exact.items():
            score = SequenceMatcher(None, name_lower, alias.lower()).ratio() * 100
            if score > best_score:
                best_score = score
                best_match = canonical

        if best_score >= self._fuzzy_threshold:
            return best_match
        return None

    def _deduplicate(self, triples: list[ResolvedTriple]) -> list[ResolvedTriple]:
        seen: dict[tuple[str, str, str], ResolvedTriple] = {}
        for triple in triples:
            key = triple.key()
            if key in seen:
                self._stats["duplicates_merged"] += 1
                if triple.confidence > seen[key].confidence:
                    seen[key] = triple
            else:
                seen[key] = triple
        return list(seen.values())

    def get_stats(self) -> dict:
        return dict(self._stats)

    def get_unresolved(self) -> list[str]:
        return list(self._unresolved)

    def reset_stats(self) -> None:
        self._stats = {
            "resolved_exact": 0,
            "resolved_fuzzy": 0,
            "unresolved": 0,
            "duplicates_merged": 0,
        }
        self._unresolved = []
