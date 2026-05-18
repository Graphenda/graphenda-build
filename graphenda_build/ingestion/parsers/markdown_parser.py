"""Parser de arquivos Markdown por secoes semanticas.

Divide por headers H2, preserva subsecoes H3, extrai front matter YAML.
"""
import hashlib
import logging
import re
from pathlib import Path

from graphenda_build.core.base_parser import BaseDocumentParser
from graphenda_shared.models.core import Chunk, ChunkType

logger = logging.getLogger(__name__)


class MarkdownDocumentParser(BaseDocumentParser):
    """Parser de .md — domain-agnostic."""

    def __init__(self, min_content_length: int = 50) -> None:
        self._min_length = min_content_length

    def supported_extensions(self) -> list[str]:
        return [".md"]

    def parse(self, file_path: Path) -> list[Chunk]:
        file_path = Path(file_path)
        if not file_path.exists():
            logger.warning("Arquivo nao encontrado: %s", file_path)
            return []

        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            logger.warning("Erro de decode: %s", file_path)
            return []

        front_matter = self._extract_front_matter(content)
        content_body = self._strip_front_matter(content)

        if not content_body.strip():
            return []

        sections = self._split_into_sections(content_body)
        doc_title = front_matter.get("title", file_path.stem)

        chunks: list[Chunk] = []
        for section in sections:
            if len(section["content"].strip()) < self._min_length:
                continue

            chunks.append(Chunk(
                chunk_id=self._make_id(file_path, section["title"]),
                content=section["content"],
                chunk_type=ChunkType.MARKDOWN_SECTION,
                source_file=str(file_path),
                metadata={
                    "name": section["title"],
                    "heading_level": section["level"],
                    "document_title": doc_title,
                    "front_matter": front_matter,
                    "has_code_blocks": "```" in section["content"],
                    "has_tables": "|" in section["content"] and "---" in section["content"],
                    "subsections": section.get("subsections", []),
                },
            ))

        logger.debug("Parsed %s: %d chunks", file_path.name, len(chunks))
        return chunks

    def _extract_front_matter(self, content: str) -> dict:
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not match:
            return {}
        result: dict[str, str] = {}
        for line in match.group(1).split("\n"):
            if ":" in line:
                key, _, value = line.partition(":")
                result[key.strip()] = value.strip().strip('"').strip("'")
        return result

    def _strip_front_matter(self, content: str) -> str:
        return re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, count=1, flags=re.DOTALL)

    def _split_into_sections(self, content: str) -> list[dict]:
        lines = content.split("\n")
        sections: list[dict] = []
        current_section: dict | None = None
        current_lines: list[str] = []
        current_subsections: list[str] = []

        for line in lines:
            if re.match(r"^# [^#]", line):
                if current_section is not None:
                    current_section["content"] = "\n".join(current_lines).strip()
                    current_section["subsections"] = current_subsections
                    sections.append(current_section)
                current_section = {"title": line.lstrip("# ").strip(), "level": 1}
                current_lines = [line]
                current_subsections = []
                continue

            if re.match(r"^## [^#]", line):
                if current_section is not None:
                    current_section["content"] = "\n".join(current_lines).strip()
                    current_section["subsections"] = current_subsections
                    sections.append(current_section)
                current_section = {"title": line.lstrip("# ").strip(), "level": 2}
                current_lines = [line]
                current_subsections = []
                continue

            if re.match(r"^### [^#]", line):
                current_subsections.append(line.lstrip("# ").strip())

            current_lines.append(line)

        if current_section is not None:
            current_section["content"] = "\n".join(current_lines).strip()
            current_section["subsections"] = current_subsections
            sections.append(current_section)

        if not sections and content.strip():
            sections.append({
                "title": "Content",
                "level": 0,
                "content": content.strip(),
                "subsections": [],
            })

        return sections

    @staticmethod
    def _make_id(file_path: Path, title: str) -> str:
        key = f"{file_path}::{title}"
        return hashlib.sha256(key.encode()).hexdigest()[:16]
