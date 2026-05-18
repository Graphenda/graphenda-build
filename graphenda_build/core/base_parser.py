"""Abstract base class para parsers de documentos.

Parsers transformam arquivos em chunks para ingestao.
Novos parsers (PDF, CSV, etc.) implementam esta interface
e se registram no ParserRegistry.
"""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graphenda_shared.models.core import Chunk


class BaseDocumentParser(ABC):
    """Interface base para parsers de documentos."""

    @abstractmethod
    def parse(self, file_path: Path) -> list["Chunk"]:
        """Transforma um arquivo em lista de chunks.

        Args:
            file_path: Caminho absoluto do arquivo.

        Returns:
            Lista de Chunk extraidos do arquivo.
        """
        ...

    @abstractmethod
    def supported_extensions(self) -> list[str]:
        """Extensoes de arquivo suportadas (ex: ['.py', '.pyx']).

        Returns:
            Lista de extensoes com ponto (ex: ['.md']).
        """
        ...
