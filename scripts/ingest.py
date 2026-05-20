"""Script CLI para ingestao de documentos em um grafo.

Uso:
    python scripts/ingest.py \
        --instance model_intelligence \
        --ontology model_intelligence \
        --source ./documentos/ \
        --file-types .py .md .pdf

    python scripts/ingest.py \
        --instance model_intelligence \
        --ontology model_intelligence \
        --source ./papers/ \
        --file-types .pdf \
        --batch-size 20

Pipeline completo:
    1. create_instance.py  → cria database + schema + seeds
    2. ingest.py           → ingere documentos → triples → Neo4j
    3. build_hierarchy.py  → levels + communities + meta-communities
"""

import argparse
import logging
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Ingerir documentos em um grafo Graphenda")
    parser.add_argument("--instance", required=True, help="Nome da instancia Neo4j")
    parser.add_argument("--ontology", required=True, help="Nome da ontologia")
    parser.add_argument(
        "--source", required=True, nargs="+",
        help="Diretorio(s) com documentos para ingerir"
    )
    parser.add_argument(
        "--file-types", nargs="+", default=[".py", ".md"],
        help="Tipos de arquivo para processar (default: .py .md)"
    )
    parser.add_argument("--batch-size", type=int, default=50, help="Batch size para extracao")
    parser.add_argument(
        "--model", default=None,
        help="Modelo LLM (override; default = configurado no provider via env)"
    )
    parser.add_argument("--dry-run", action="store_true", help="Extrair triples sem carregar no Neo4j")
    parser.add_argument("--full", action="store_true", help="Modo full (ignora cache incremental)")
    args = parser.parse_args()

    from graphenda_shared.graph.connection import Neo4jConnection
    from graphenda_build.llm import provider_from_env
    from graphenda_build.ontology.manager import OntologyRegistry
    from graphenda_build.ingestion.pipeline import IngestPipeline

    project_root = Path(__file__).resolve().parent.parent
    ontologies_dir = project_root / "ontologies"

    # 1. Carregar ontologia
    print(f"Ontologia: {args.ontology}")
    registry = OntologyRegistry(ontologies_dir)
    ontology = registry.load(args.ontology)

    # 2. Conectar ao Neo4j
    neo4j = None
    if not args.dry_run:
        print(f"Conectando ao Neo4j (database: {args.instance})")
        neo4j = Neo4jConnection(database=args.instance)
        result = neo4j.run("MATCH (n) RETURN count(n) AS count")
        existing = result[0]["count"] if result else 0
        print(f"  Nodes existentes: {existing}")

    # 3. Configurar source dirs
    source_dirs = [
        {"path": src, "file_types": args.file_types}
        for src in args.source
    ]

    # 4. Rodar pipeline
    print(f"\nIniciando pipeline...")
    print(f"  Sources: {args.source}")
    print(f"  File types: {args.file_types}")
    print(f"  Batch size: {args.batch_size}")
    print(f"  Mode: {'full' if args.full else 'incremental'}")
    print(f"  Dry run: {args.dry_run}")
    print()

    llm = provider_from_env()
    print(f"LLM provider: {llm.name} (model: {args.model or llm.model})")

    pipeline = IngestPipeline(
        ontology=ontology,
        neo4j=neo4j,
        llm=llm,
        model=args.model,
        batch_size=args.batch_size,
    )

    stats = pipeline.run(
        source_dirs=source_dirs,
        incremental=not args.full,
        dry_run=args.dry_run,
        batch_size=args.batch_size,
    )

    # 5. Relatorio
    print(pipeline.get_report())

    # 6. Mostrar triples se dry-run
    if args.dry_run:
        triples = pipeline.get_triples()
        if triples:
            print(f"\nPrimeiros 10 triples:")
            for t in triples[:10]:
                print(f"  {t.subject} ({t.subject_type}) --[{t.predicate}]--> {t.object} ({t.object_type})  conf={t.confidence:.2f}")

    if neo4j:
        # Verificar resultado final
        result = neo4j.run("MATCH (n) RETURN count(n) AS count")
        final_nodes = result[0]["count"] if result else 0
        result = neo4j.run("MATCH ()-[r]->() RETURN count(r) AS count")
        final_rels = result[0]["count"] if result else 0
        print(f"\nEstado final do grafo:")
        print(f"  Nodes: {final_nodes}")
        print(f"  Relationships: {final_rels}")
        neo4j.close()

    print("\nProximo passo: construir hierarquia com:")
    print(f"  python scripts/build_hierarchy.py --ontology {args.ontology} --instance {args.instance}")


if __name__ == "__main__":
    main()
