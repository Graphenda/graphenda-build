"""Parser basico de arquivos CSV.

Extrai metadados do dataset: colunas, tipos, amostras.
Util para ingestar metadata de datasets tabulares.
"""
import csv
import hashlib
import logging
from pathlib import Path

from graphenda_build.core.base_parser import BaseDocumentParser
from graphenda_shared.models.core import Chunk, ChunkType

logger = logging.getLogger(__name__)


class CsvDocumentParser(BaseDocumentParser):
    """Parser de .csv — extrai metadata do dataset."""

    def __init__(self, sample_rows: int = 5) -> None:
        self._sample_rows = sample_rows

    def supported_extensions(self) -> list[str]:
        return [".csv"]

    def parse(self, file_path: Path) -> list[Chunk]:
        file_path = Path(file_path)
        if not file_path.exists():
            logger.warning("Arquivo nao encontrado: %s", file_path)
            return []

        try:
            with open(file_path, encoding="utf-8", newline="") as f:
                reader = csv.reader(f)
                rows = list(reader)
        except (UnicodeDecodeError, csv.Error) as e:
            logger.warning("Erro ao parsear CSV %s: %s", file_path, e)
            return []

        if not rows:
            return []

        headers = rows[0] if rows else []
        data_rows = rows[1:]
        sample = data_rows[: self._sample_rows]

        # Monta descricao textual do dataset
        lines = [
            f"Dataset: {file_path.stem}",
            f"Columns ({len(headers)}): {', '.join(headers)}",
            f"Rows: {len(data_rows)}",
            "",
            "Sample data:",
        ]
        for row in sample:
            row_desc = ", ".join(
                f"{h}={v}" for h, v in zip(headers, row) if v.strip()
            )
            lines.append(f"  {row_desc}")

        content = "\n".join(lines)

        chunk = Chunk(
            chunk_id=self._make_id(file_path),
            content=content,
            chunk_type=ChunkType.CSV_METADATA,
            source_file=str(file_path),
            metadata={
                "name": file_path.stem,
                "columns": headers,
                "row_count": len(data_rows),
                "sample_rows": self._sample_rows,
            },
        )

        logger.debug("Parsed %s: 1 chunk (%d colunas, %d linhas)", file_path.name, len(headers), len(data_rows))
        return [chunk]

    @staticmethod
    def _make_id(file_path: Path) -> str:
        key = f"{file_path}::csv_metadata"
        return hashlib.sha256(key.encode()).hexdigest()[:16]
