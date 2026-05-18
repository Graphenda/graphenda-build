"""Inter-Level Linker: cria relacoes explicitas entre niveis hierarquicos.

Deriva ABSTRACTS (L2->L1) e GROUPS (L3->L2) a partir de relacoes existentes.
PART_OF (L4->L3) e criado pelo MetaCommunityBuilder (F2.3).

Domain-agnostic: le os tipos de relacao da ontologia em vez de hardcoda-los.
"""
import logging

logger = logging.getLogger(__name__)


class InterLevelLinker:
    """Cria relacoes inter-nivel derivadas das relacoes existentes."""

    def __init__(self, ontology, neo4j):
        """
        Args:
            ontology: OntologySchema carregado.
            neo4j: Neo4jConnection ativa.
        """
        self.ontology = ontology
        self.neo4j = neo4j
        self._hierarchy_rels = getattr(ontology, "hierarchy_relationships", {})

    def link_all(self):
        """Cria todas as relacoes inter-nivel (exceto PART_OF)."""
        self._link_l2_to_l1()
        self._link_l3_to_l2()

    def _get_derived_from(self, rel_name: str) -> list[str]:
        """Obtem lista de relationship types usados para derivar uma relacao.

        Le de hierarchy_relationships da ontologia. Se nao configurado,
        descobre automaticamente relacoes cross-level entre os niveis.
        """
        config = self._hierarchy_rels.get(rel_name, {})
        derived = config.get("auto_derived_from", [])
        if derived:
            # Filtrar compound rules (ex: "BELONGS_TO+ADDRESSES")
            return [r for r in derived if "+" not in r]
        return []

    def _discover_cross_level_rels(self, level_a: int, level_b: int) -> list[str]:
        """Descobre relacoes cross-level entre dois niveis via ontologia."""
        rels = []
        for rel_name, rel_cfg in self.ontology.relationship_types.items():
            if not rel_cfg.cross_level:
                continue
            src = rel_cfg.source
            tgt = rel_cfg.target
            if src in self.ontology.entity_types and tgt in self.ontology.entity_types:
                src_level = self.ontology.entity_types[src].level
                tgt_level = self.ontology.entity_types[tgt].level
                if {src_level, tgt_level} == {level_a, level_b}:
                    rels.append(rel_name)
        return rels

    def _link_l2_to_l1(self):
        """ABSTRACTS: Level 2 -> Level 1.

        Derivado de relacoes cross-level entre L1 e L2 (ex: TESTS_FOR, ADDRESSES).
        Relacoes existentes como (L1)-[:ADDRESSES]->(L2) geram (L2)-[:ABSTRACTS]->(L1).
        """
        rel_types = self._get_derived_from("ABSTRACTS")
        if not rel_types:
            rel_types = self._discover_cross_level_rels(1, 2)

        if not rel_types:
            logger.warning("Nenhuma relacao cross-level encontrada entre L1 e L2")
            return

        logger.info("ABSTRACTS derivado de: %s", rel_types)

        # Relacoes existentes vao de L1->L2 (ex: Estimator-[:ADDRESSES]->StatisticalConcept)
        # ABSTRACTS vai de L2->L1, entao invertemos a direcao
        self.neo4j.run(
            """
            MATCH (fact)-[r]->(concept)
            WHERE fact.level = 1 AND concept.level = 2
            AND type(r) IN $rel_types
            MERGE (concept)-[:ABSTRACTS]->(fact)
            """,
            {"rel_types": rel_types},
        )

    def _link_l3_to_l2(self):
        """GROUPS: Level 3 -> Level 2.

        Derivado de padroes compostos (ex: BELONGS_TO + ADDRESSES).
        Se (L3)<-[:BELONGS_TO]-(L1_entity)-[:ADDRESSES]->(L2),
        entao (L3)-[:GROUPS]->(L2).

        Descobre automaticamente os padroes de ligacao via entidades intermediarias.
        """
        # Buscar relacoes L1->L3 e L1->L2 para encontrar entidades intermediarias
        rels_l1_to_l3 = self._find_rels_between_levels(1, 3)
        rels_l1_to_l2 = self._find_rels_between_levels(1, 2)

        if not rels_l1_to_l3 or not rels_l1_to_l2:
            logger.warning(
                "Relacoes insuficientes para derivar GROUPS: "
                "L1->L3=%s, L1->L2=%s", rels_l1_to_l3, rels_l1_to_l2
            )
            return

        logger.info("GROUPS derivado de: %s + %s", rels_l1_to_l3, rels_l1_to_l2)

        self.neo4j.run(
            """
            MATCH (family)<-[r1]-(entity)-[r2]->(concept)
            WHERE family.level = 3 AND concept.level = 2
            AND type(r1) IN $rels_to_family
            AND type(r2) IN $rels_to_concept
            MERGE (family)-[:GROUPS]->(concept)
            """,
            {"rels_to_family": rels_l1_to_l3, "rels_to_concept": rels_l1_to_l2},
        )

    def _find_rels_between_levels(
        self, source_level: int, target_level: int
    ) -> list[str]:
        """Encontra relationship types entre dois niveis especificos."""
        rels = []
        for rel_name, rel_cfg in self.ontology.relationship_types.items():
            src = rel_cfg.source
            tgt = rel_cfg.target
            if src in self.ontology.entity_types and tgt in self.ontology.entity_types:
                src_lvl = self.ontology.entity_types[src].level
                tgt_lvl = self.ontology.entity_types[tgt].level
                if src_lvl == source_level and tgt_lvl == target_level:
                    rels.append(rel_name)
        return rels

    def verify(self) -> dict:
        """Conta relacoes inter-nivel criadas.

        Returns:
            Dict com tipo de relacao -> contagem.
            Ex: {"ABSTRACTS": 45, "GROUPS": 12}
        """
        result = self.neo4j.run("""
            MATCH ()-[r]->()
            WHERE type(r) IN ['ABSTRACTS', 'GROUPS', 'PART_OF']
            RETURN type(r) AS rel_type, count(r) AS count
        """)
        return {r["rel_type"]: r["count"] for r in result}

    def verify_traversal(self) -> bool:
        """Verifica que traversal L3->L2->L1 e funcional.

        Returns:
            True se pelo menos um caminho completo L3->L2->L1 existe.
        """
        result = self.neo4j.run("""
            MATCH (l3)-[:GROUPS]->(l2)-[:ABSTRACTS]->(l1)
            WHERE l3.level = 3 AND l2.level = 2 AND l1.level = 1
            RETURN count(*) AS paths
            LIMIT 1
        """)
        return result[0]["paths"] > 0 if result else False
