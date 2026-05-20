"""Script CLI para criacao de instancias.

Uso:
    python scripts/create_instance.py \
        --name model_intelligence \
        --ontology model_intelligence \
        --seed
"""

import argparse
import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class InstanceConfig:
    """Configuracao minima de instancia para o InstanceNeo4jManager."""
    name: str
    neo4j_database: str


def main():
    parser = argparse.ArgumentParser(description="Criar instancia Graphenda")
    parser.add_argument("--name", required=True, help="Nome da instancia")
    parser.add_argument("--ontology", required=True, help="Nome da ontologia")
    parser.add_argument(
        "--seed", action="store_true", help="Carregar seed entities"
    )
    parser.add_argument(
        "--strategy", default="database", choices=["database", "prefix"],
        help="Estrategia de isolamento Neo4j (default: database)"
    )
    parser.add_argument(
        "--drop", action="store_true",
        help="Dropar instancia existente antes de criar"
    )
    args = parser.parse_args()

    from graphenda_shared.graph.connection import Neo4jConnection
    from graphenda_build.graph.instance_manager import InstanceNeo4jManager
    from graphenda_build.graph.loader import GraphLoader
    from graphenda_build.graph.schema import SchemaBuilder
    from graphenda_build.ontology.manager import OntologyRegistry

    project_root = Path(__file__).resolve().parent.parent
    ontologies_dir = project_root / "ontologies"

    # 1. Carregar ontologia
    print(f"[1/5] Carregando ontologia: {args.ontology}")
    ontology_registry = OntologyRegistry(ontologies_dir=ontologies_dir)
    try:
        ontology = ontology_registry.load(args.ontology)
    except Exception as e:
        logger.error("Falha ao carregar ontologia '%s': %s", args.ontology, e)
        sys.exit(1)
    print(f"  Entity types: {len(ontology.entity_types)}")
    print(f"  Relationship types: {len(ontology.relationship_types)}")
    print(f"  Aliases: {len(ontology.aliases)}")

    # 2. Criar instancia no Neo4j
    print(f"\n[2/5] Criando instancia Neo4j: {args.name} (strategy={args.strategy})")
    neo4j = Neo4jConnection()
    manager = InstanceNeo4jManager(neo4j, strategy=args.strategy)
    instance = InstanceConfig(name=args.name, neo4j_database=args.name)

    try:
        if args.drop:
            print(f"  Dropando instancia existente: {args.name}")
            manager.delete_instance_graph(instance)

        manager.create_instance_graph(instance, ontology=ontology)
        print(f"  Database '{args.name}' criado/verificado")
    except Exception as e:
        logger.error("Falha ao criar instancia: %s", e)
        neo4j.close()
        sys.exit(1)

    # 3. Inicializar schema
    print("\n[3/5] Inicializando schema (constraints + indexes)")
    conn = manager.get_connection(instance)
    schema_builder = SchemaBuilder(conn=conn, ontology=ontology)
    schema_result = schema_builder.initialize()
    print(f"  Constraints: {schema_result['constraints']}")
    print(f"  Indexes: {schema_result['indexes']}")

    # 4. Carregar seed entities (opcional)
    if args.seed:
        print("\n[4/5] Carregando seed entities")
        loader = GraphLoader(conn=conn, ontology=ontology)
        n_ent, n_rel = loader.load_seed_data()
        print(f"  Entities: {n_ent}")
        print(f"  Relationships: {n_rel}")
    else:
        print("\n[4/5] Seed entities: pulado (use --seed para carregar)")

    # 5. Verificacao
    print("\n[5/5] Verificando instancia")
    result = conn.run("MATCH (n) RETURN count(n) AS nodes")
    node_count = result[0]["nodes"] if result else 0
    result = conn.run("MATCH ()-[r]->() RETURN count(r) AS rels")
    rel_count = result[0]["rels"] if result else 0
    print(f"  Nodes: {node_count}")
    print(f"  Relationships: {rel_count}")

    manager.close_all()
    neo4j.close()

    print(f"\nInstancia '{args.name}' criada com sucesso!")
    print(f"\nProximo passo: ingerir documentos com:")
    print(f"  python scripts/ingest.py --instance {args.name} --ontology {args.ontology} --source ./documentos/")


if __name__ == "__main__":
    main()
