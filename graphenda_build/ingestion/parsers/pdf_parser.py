"""Parser basico de arquivos PDF.

Extrai texto por paginas e agrupa em secoes.
Requer PyPDF2 ou pdfplumber (fallback para texto simples).
"""
import hashlib
import logging
from pathlib import Path

from graphenda_build.core.base_parser import BaseDocumentParser
from graphenda_shared.models.core import Chunk, ChunkType

logger = logging.getLogger(__name__)


class PdfDocumentParser(BaseDocumentParser):
    """Parser de .pdf — extrai texto por paginas."""

    def __init__(self, pages_per_chunk: int = 3) -> None:
        self._pages_per_chunk = pages_per_chunk

    def supported_extensions(self) -> list[str]:
        return [".pdf"]

    def parse(self, file_path: Path) -> list[Chunk]:
        file_path = Path(file_path)
        if not file_path.exists():
            logger.warning("Arquivo nao encontrado: %s", file_path)
            return []

        pages = self._extract_pages(file_path)
        if not pages:
            return []

        chunks: list[Chunk] = []
        for i in range(0, len(pages), self._pages_per_chunk):
            page_group = pages[i : i + self._pages_per_chunk]
            content = "\n\n".join(page_group)

            if len(content.strip()) < 50:
                continue

            start_page = i + 1
            end_page = min(i + self._pages_per_chunk, len(pages))

            chunks.append(Chunk(
                chunk_id=self._make_id(file_path, start_page),
                content=content,
                chunk_type=ChunkType.PDF_SECTION,
                source_file=str(file_path),
                metadata={
                    "name": f"Pages {start_page}-{end_page}",
                    "document_title": file_path.stem,
                    "page_start": start_page,
                    "page_end": end_page,
                    "total_pages": len(pages),
                },
            ))

        logger.debug("Parsed %s: %d chunks from %d pages", file_path.name, len(chunks), len(pages))
        return chunks

    def _extract_pages(self, file_path: Path) -> list[str]:
        """Extrai texto de cada pagina do PDF."""
        # Tenta PyPDF2
        try:
            from PyPDF2 import PdfReader  # type: ignore[import-untyped]

            reader = PdfReader(str(file_path))
            return [page.extract_text() or "" for page in reader.pages]
        except ImportError:
            pass
        except Exception as e:
            logger.warning("PyPDF2 falhou para %s: %s", file_path, e)

        # Tenta pdfplumber
        try:
            import pdfplumber  # type: ignore[import-untyped]

            with pdfplumber.open(file_path) as pdf:
                return [page.extract_text() or "" for page in pdf.pages]
        except ImportError:
            pass
        except Exception as e:
            logger.warning("pdfplumber falhou para %s: %s", file_path, e)

        logger.warning(
            "Nenhuma biblioteca PDF disponivel (PyPDF2 ou pdfplumber). "
            "Instale com: pip install PyPDF2 ou pip install pdfplumber"
        )
        return []

    @staticmethod
    def _make_id(file_path: Path, start_page: int) -> str:
        key = f"{file_path}::page_{start_page}"
        return hashlib.sha256(key.encode()).hexdigest()[:16]
