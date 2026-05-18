"""Registry de parsers plugaveis.

Mapeia extensoes de arquivo para implementacoes de BaseDocumentParser.
Permite registro dinamico de novos parsers em runtime.
"""
import logging
from pathlib import Path
from typing import TYPE_CHECKING

from graphenda_build.core.base_parser import BaseDocumentParser

if TYPE_CHECKING:
    from graphenda_shared.models.core import Chunk

logger = logging.getLogger(__name__)


class ParserRegistry:
    """Registro central de parsers de documentos.

    Mapeia extensoes (.py, .md, etc.) para instancias de BaseDocumentParser.
    Suporta registro dinamico e criacao de registry com parsers padrao.
    """

    def __init__(self) -> None:
        self._parsers: dict[str, BaseDocumentParser] = {}

    def register(self, parser: BaseDocumentParser) -> None:
        """Registra um parser para todas as suas extensoes suportadas.

        Args:
            parser: Instancia de BaseDocumentParser.
        """
        for ext in parser.supported_extensions():
            ext = ext.lower()
            if ext in self._parsers:
                logger.warning(
                    "Sobrescrevendo parser para '%s': %s -> %s",
                    ext,
                    type(self._parsers[ext]).__name__,
                    type(parser).__name__,
                )
            self._parsers[ext] = parser
            logger.debug("Parser registrado: %s -> %s", ext, type(parser).__name__)

    def get_parser(self, file_path: Path) -> BaseDocumentParser | None:
        """Retorna o parser adequado para um arquivo.

        Args:
            file_path: Caminho do arquivo.

        Returns:
            Parser correspondente ou None.
        """
        ext = Path(file_path).suffix.lower()
        return self._parsers.get(ext)

    def parse(self, file_path: Path) -> list["Chunk"]:
        """Parseia um arquivo usando o parser registrado.

        Args:
            file_path: Caminho do arquivo.

        Returns:
            Lista de chunks extraidos.

        Raises:
            ValueError: Se nao houver parser para a extensao.
        """
        parser = self.get_parser(file_path)
        if parser is None:
            raise ValueError(f"Nenhum parser registrado para extensao '{file_path.suffix}'")
        return parser.parse(file_path)

    @property
    def supported_extensions(self) -> list[str]:
        """Lista de extensoes suportadas."""
        return sorted(self._parsers.keys())

    @classmethod
    def default(cls) -> "ParserRegistry":
        """Cria registry com todos os parsers padrao registrados.

        Returns:
            ParserRegistry com parsers .py, .md, .ipynb, .pdf, .csv.
        """
        from graphenda_build.ingestion.parsers.python_parser import PythonDocumentParser
        from graphenda_build.ingestion.parsers.markdown_parser import MarkdownDocumentParser
        from graphenda_build.ingestion.parsers.notebook_parser import NotebookDocumentParser
        from graphenda_build.ingestion.parsers.pdf_parser import PdfDocumentParser
        from graphenda_build.ingestion.parsers.csv_parser import CsvDocumentParser

        registry = cls()
        registry.register(PythonDocumentParser())
        registry.register(MarkdownDocumentParser())
        registry.register(NotebookDocumentParser())
        registry.register(PdfDocumentParser())
        registry.register(CsvDocumentParser())

        logger.info(
            "ParserRegistry criado com %d extensoes: %s",
            len(registry._parsers),
            registry.supported_extensions,
        )
        return registry
