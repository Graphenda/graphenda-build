"""Script para construir a hierarquia cognitiva completa.

Uso:
    python scripts/build_hierarchy.py --ontology model_intelligence
    python scripts/build_hierarchy.py --ontology model_intelligence --instance model_intelligence
    python scripts/build_hierarchy.py --ontology model_intelligence --skip-meta

Etapas:
    1. Assign levels a todos os nodes
    2. Cria inter-level relations (ABSTRACTS, GROUPS)
    3. Detecta communities (Leiden)
    4. Build meta-communities / Knowledge Systems (opcional)
    5. Verifica hierarquia completa
"""
import argparse
import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Build cognitive hierarchy")
    parser.add_argument(
        "--ontology", required=True,
        help="Nome da ontologia (ex: model_intelligence)"
    )
    parser.add_argument(
        "--instance", default=None,
        help="Nome da instancia Neo4j (default: mesmo que ontologia)"
    )
    parser.add_argument(
        "--skip-meta", action="store_true",
        help="Pular criacao de meta-communities (Level 4)"
    )
    parser.add_argument(
        "--skip-communities", action="store_true",
        help="Pular deteccao de communities"
    )
    parser.add_argument(
        "--resolution", type=float, default=1.0,
        help="Resolucao do Leiden para community detection (default: 1.0)"
    )
    args = parser.parse_args()

    instance_name = args.instance or args.ontology

    from graphenda_shared.graph.connection import Neo4jConnection
    from graphenda_build.llm import provider_from_env
    from graphenda_build.ontology.manager import OntologyRegistry
    from graphenda_build.hierarchy.level_assigner import LevelAssigner
    from graphenda_build.hierarchy.inter_level_linker import InterLevelLinker

    project_root = Path(__file__).resolve().parent.parent
    ontologies_dir = project_root / "ontologies"

    # 1. Carregar ontologia
    print(f"[1/5] Loading ontology: {args.ontology}")
    registry = OntologyRegistry(ontologies_dir)
    ontology = registry.load(args.ontology)
    print(f"  Entity types: {len(ontology.entity_types)}")

    # Conectar ao Neo4j
    neo4j = Neo4jConnection(database=instance_name)

    # Verificar que existem nodes
    result = neo4j.run("MATCH (n) RETURN count(n) AS count")
    node_count = result[0]["count"] if result else 0
    if node_count == 0:
        print(f"  ERRO: Nenhum node encontrado no database '{instance_name}'.")
        print(f"  Execute primeiro: python scripts/ingest.py --instance {instance_name} ...")
        neo4j.close()
        sys.exit(1)
    print(f"  Nodes no grafo: {node_count}")

    # 2. Assign levels
    print("\n[2/5] Assigning levels...")
    assigner = LevelAssigner(ontology, neo4j)
    assigner.assign_all()
    assigner.create_index()
    stats = assigner.verify()
    print(f"  Levels: {stats}")
    unassigned = assigner.find_unassigned()
    if unassigned:
        print(f"  WARNING: {len(unassigned)} unassigned nodes:")
        for node in unassigned[:5]:
            print(f"    - {node}")
    else:
        print("  Todos os nodes com level atribuido")

    # 3. Inter-level relations
    print("\n[3/5] Creating inter-level relations...")
    linker = InterLevelLinker(ontology, neo4j)
    linker.link_all()
    link_stats = linker.verify()
    print(f"  Relations created: {link_stats}")

    # 4. Community detection
    if not args.skip_communities:
        print(f"\n[4/5] Detecting communities (resolution={args.resolution})...")
        try:
            from graphenda_build.community.detector import CommunityDetector
            detector = CommunityDetector(neo4j)
            community_stats = detector.detect(resolution=args.resolution)
            print(f"  Communities: {community_stats.get('community_count', 0)}")
            print(f"  Modularity: {community_stats.get('modularity', 0):.3f}")
        except ImportError:
            print("  WARNING: igraph/leidenalg not installed. Skipping community detection.")
            print("  Install with: pip install igraph leidenalg")
        except Exception as e:
            print(f"  WARNING: Community detection failed: {e}")
    else:
        print("\n[4/5] Skipping community detection (--skip-communities)")

    # 5. Meta-communities (Level 4)
    if not args.skip_meta and not args.skip_communities:
        print("\n[5/5] Building meta-communities (Level 4)...")
        try:
            from graphenda_build.hierarchy.meta_community import MetaCommunityBuilder
            from graphenda_build.community.summarizer import CommunitySummarizer

            llm = provider_from_env()
            print(f"  LLM provider: {llm.name} (model: {llm.model})")
            summarizer = CommunitySummarizer(neo4j, llm=llm, ontology=ontology)
            builder = MetaCommunityBuilder(neo4j, summarizer)
            builder.build(resolution=0.5)
            meta_stats = builder.verify()
            print(f"  Knowledge Systems: {meta_stats.get('system_count', 0)}")
            print(f"  PART_OF relations: {meta_stats.get('part_of_count', 0)}")
        except ImportError:
            print("  WARNING: Dependencies not installed. Skipping meta-communities.")
        except Exception as e:
            print(f"  WARNING: Meta-community building failed: {e}")
    else:
        print("\n[5/5] Skipping meta-communities")

    # Verificacao final
    print("\n" + "=" * 50)
    print("HIERARCHY SUMMARY")
    print("=" * 50)
    for level in range(1, 5):
        result = neo4j.run(
            "MATCH (n) WHERE n.level = $level RETURN count(n) AS count",
            {"level": level}
        )
        count = result[0]["count"] if result else 0
        labels = {
            1: "Facts", 2: "Concepts", 3: "Domains", 4: "Systems"
        }
        print(f"  L{level} ({labels[level]}): {count} nodes")

    # Contar relacoes inter-nivel
    for rel_type in ["ABSTRACTS", "GROUPS", "PART_OF"]:
        result = neo4j.run(
            f"MATCH ()-[r:{rel_type}]->() RETURN count(r) AS count"
        )
        count = result[0]["count"] if result else 0
        print(f"  {rel_type}: {count} relations")

    neo4j.close()
    print("\nHierarchy build complete!")


if __name__ == "__main__":
    main()
