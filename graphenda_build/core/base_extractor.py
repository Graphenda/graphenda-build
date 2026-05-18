"""Abstract base class para extractors de triples.

Extractors transformam chunks em triples (subject, predicate, object)
usando a ontologia como guia para validacao.
"""
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graphenda_shared.models.core import Chunk, Triple
    from graphenda_build.ontology.manager import OntologySchema


class BaseTripleExtractor(ABC):
    """Interface base para extractors de triples."""

    @abstractmethod
    def extract(self, chunks: list["Chunk"], ontology: "OntologySchema") -> list["Triple"]:
        """Extrai triples de chunks usando a ontologia como guia.

        Args:
            chunks: Lista de chunks a processar.
            ontology: Schema da ontologia ativa.

        Returns:
            Lista de Triple extraidos.
        """
        ...
