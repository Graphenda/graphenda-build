"""Parser de Jupyter Notebooks para chunking semantico.

Agrupa celulas adjacentes em unidades narrativas:
markdown + codigo formam um chunk.
"""
import hashlib
import json
import logging
from pathlib import Path

from graphenda_build.core.base_parser import BaseDocumentParser
from graphenda_shared.models.core import Chunk, ChunkType

logger = logging.getLogger(__name__)


class NotebookDocumentParser(BaseDocumentParser):
    """Parser de .ipynb — domain-agnostic."""

    def __init__(self, max_tokens_per_chunk: int = 2000) -> None:
        self._max_tokens = max_tokens_per_chunk

    def supported_extensions(self) -> list[str]:
        return [".ipynb"]

    def parse(self, file_path: Path) -> list[Chunk]:
        file_path = Path(file_path)
        if not file_path.exists():
            logger.warning("Arquivo nao encontrado: %s", file_path)
            return []

        try:
            with open(file_path, encoding="utf-8") as f:
                notebook = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            logger.warning("Erro ao parsear notebook %s: %s", file_path, e)
            return []

        cells = notebook.get("cells", [])
        if not cells:
            return []

        groups = self._group_cells(cells)
        chunks: list[Chunk] = []

        for i, group in enumerate(groups):
            content = self._format_cell_group(group)
            if not content.strip() or len(content) < 30:
                continue

            title = self._extract_group_title(group, i)

            chunks.append(Chunk(
                chunk_id=self._make_id(file_path, i),
                content=content,
                chunk_type=ChunkType.NOTEBOOK_CELL_GROUP,
                source_file=str(file_path),
                metadata={
                    "name": title,
                    "notebook": file_path.stem,
                    "group_index": i,
                    "n_cells": len(group),
                    "cell_types": [c.get("cell_type", "unknown") for c in group],
                    "has_code": any(c.get("cell_type") == "code" for c in group),
                    "has_markdown": any(c.get("cell_type") == "markdown" for c in group),
                },
            ))

        logger.debug("Parsed %s: %d chunks from %d cells", file_path.name, len(chunks), len(cells))
        return chunks

    def _group_cells(self, cells: list[dict]) -> list[list[dict]]:
        groups: list[list[dict]] = []
        current_group: list[dict] = []
        current_tokens = 0

        for cell in cells:
            cell_content = self._get_cell_source(cell)
            cell_tokens = len(cell_content) // 4

            if not cell_content.strip():
                continue

            cell_type = cell.get("cell_type", "")

            if cell_type == "markdown":
                if current_group and current_tokens > 100:
                    groups.append(current_group)
                    current_group = []
                    current_tokens = 0
                current_group.append(cell)
                current_tokens += cell_tokens

            elif cell_type == "code":
                if current_tokens + cell_tokens > self._max_tokens * 4:
                    if current_group:
                        groups.append(current_group)
                    current_group = [cell]
                    current_tokens = cell_tokens
                else:
                    current_group.append(cell)
                    current_tokens += cell_tokens

        if current_group:
            groups.append(current_group)

        return groups

    def _format_cell_group(self, cells: list[dict]) -> str:
        parts: list[str] = []
        for cell in cells:
            cell_type = cell.get("cell_type", "unknown")
            source = self._get_cell_source(cell)
            if cell_type == "markdown":
                parts.append(source)
            elif cell_type == "code":
                parts.append(f"```python\n{source}\n```")
        return "\n\n".join(parts)

    @staticmethod
    def _get_cell_source(cell: dict) -> str:
        source = cell.get("source", [])
        if isinstance(source, list):
            return "".join(source)
        return str(source)

    def _extract_group_title(self, cells: list[dict], group_index: int) -> str:
        for cell in cells:
            if cell.get("cell_type") == "markdown":
                source = self._get_cell_source(cell)
                for line in source.split("\n"):
                    if line.startswith("#"):
                        return line.lstrip("# ").strip()
                for line in source.split("\n"):
                    stripped = line.strip()
                    if stripped and not stripped.startswith("!") and not stripped.startswith("<"):
                        return stripped[:80]
        return f"Cell Group {group_index + 1}"

    @staticmethod
    def _make_id(file_path: Path, group_index: int) -> str:
        key = f"{file_path}::group_{group_index}"
        return hashlib.sha256(key.encode()).hexdigest()[:16]
