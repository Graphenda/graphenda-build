"""Manager de instancias Neo4j com suporte a multiplas estrategias de isolamento.

Estrategias:
- "database": Neo4j Enterprise — cria database separado por instancia
- "prefix": Neo4j Community — usa label prefixing para isolamento
"""
from __future__ import annotations

import logging
from typing import Any, Protocol, Union

from graphenda_shared.graph.connection import Neo4jConnection

logger = logging.getLogger(__name__)


class Instance(Protocol):
    """Protocolo minimo para instancia."""
    name: str
    neo4j_database: str


class PrefixedNeo4jConnection:
    """Connection wrapper que prefixa labels para isolamento Community Edition."""

    def __init__(self, connection: Neo4jConnection, prefix: str):
        self.connection = connection
        self.prefix = prefix

    def prefixed_label(self, label: str) -> str:
        return f"{self.prefix}__{label}"

    def run(
        self, query: str, parameters: dict[str, Any] | None = None
    ) -> list[dict[str, Any]]:
        """Executa query com labels prefixados."""
        return self.connection.run(query, parameters)

    def session(self, database: str = "neo4j"):
        """Proxy para session da conexao subjacente."""
        return self.connection.session(database=database)

    def close(self) -> None:
        """No-op — a conexao subjacente e gerenciada externamente."""
        pass


class InstanceNeo4jManager:
    """Gerencia conexoes e databases Neo4j por instancia."""

    def __init__(self, neo4j: Neo4jConnection, strategy: str = "database"):
        self.neo4j = neo4j
        self.strategy = strategy  # "database" ou "prefix"
        self._pool: dict[str, Union[Neo4jConnection, PrefixedNeo4jConnection]] = {}

    def create_instance_graph(self, instance: Instance, ontology=None) -> None:
        """Cria database/schema para uma nova instancia.

        Args:
            instance: Instancia com name e neo4j_database.
            ontology: OntologySchema para construir o schema. Se None, pula criacao de schema.
        """
        if self.strategy == "database":
            self.neo4j.run(
                f"CREATE DATABASE `{instance.neo4j_database}` IF NOT EXISTS"
            )
        conn = self.get_connection(instance)
        if ontology is not None:
            from graphenda_build.graph.schema import SchemaBuilder
            schema_builder = SchemaBuilder(conn=conn, ontology=ontology)
            schema_builder.initialize()

    def get_connection(
        self, instance: Instance
    ) -> Union[Neo4jConnection, PrefixedNeo4jConnection]:
        """Retorna connection scoped e pooled para a instancia.

        Args:
            instance: Instancia alvo.

        Returns:
            Conexao Neo4j isolada para a instancia.
        """
        cache_key = instance.name
        if cache_key not in self._pool:
            if self.strategy == "database":
                self._pool[cache_key] = Neo4jConnection(
                    uri=self.neo4j._uri,
                    user=self.neo4j._user,
                    password=self.neo4j._password,
                )
            else:
                self._pool[cache_key] = PrefixedNeo4jConnection(
                    connection=self.neo4j, prefix=instance.name
                )
        return self._pool[cache_key]

    def delete_instance_graph(self, instance: Instance) -> None:
        """Remove database/dados de uma instancia.

        Args:
            instance: Instancia a remover.
        """
        if self.strategy == "database":
            self.neo4j.run(
                f"DROP DATABASE `{instance.neo4j_database}` IF EXISTS"
            )
        else:
            conn = self.get_connection(instance)
            conn.run(
                f"MATCH (n) WHERE any(l IN labels(n) "
                f"WHERE l STARTS WITH '{instance.name}__') DETACH DELETE n"
            )
        self._pool.pop(instance.name, None)

    def close_all(self) -> None:
        """Fecha todas as conexoes do pool."""
        for conn in self._pool.values():
            if hasattr(conn, "close"):
                conn.close()
        self._pool.clear()
