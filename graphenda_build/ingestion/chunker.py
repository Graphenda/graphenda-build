"""Chunker unificado que usa ParserRegistry.

Despacha arquivos para o parser correto baseado em extensao,
gerencia cache JSON por arquivo, e suporta modo incremental.
"""
import hashlib
import json
import logging
from collections import Counter
from datetime import datetime
from pathlib import Path

from graphenda_shared.models.core import Chunk
from graphenda_build.ingestion.parsers.registry import ParserRegistry

logger = logging.getLogger(__name__)


class Chunker:
    """Orchestrador de parsing com cache e modo incremental."""

    def __init__(
        self,
        registry: ParserRegistry | None = None,
        cache_dir: str | Path = "cache/chunks",
    ) -> None:
        self._registry = registry or ParserRegistry.default()
        self._cache_dir = Path(cache_dir)
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        self._stats: dict = {
            "files_processed": 0,
            "files_from_cache": 0,
            "files_skipped": 0,
            "total_chunks": 0,
            "total_tokens": 0,
            "chunks_by_type": Counter(),
            "processing_time": 0.0,
        }

    def process_sources(
        self, source_dirs: list[dict], incremental: bool = True
    ) -> list[Chunk]:
        """Processa todos os diretorios-fonte.

        Args:
            source_dirs: Lista de dicts com 'path' e 'file_types'.
            incremental: Se True, usa cache para arquivos inalterados.

        Returns:
            Todos os chunks de todos os fontes.
        """
        start_time = datetime.now()
        all_chunks: list[Chunk] = []

        for source in source_dirs:
            dir_path = Path(source["path"])
            file_types = source.get("file_types", self._registry.supported_extensions)

            if not dir_path.exists():
                logger.warning("Diretorio nao encontrado: %s", dir_path)
                continue

            logger.info("Processando: %s (types: %s)", dir_path, file_types)

            for file_type in file_types:
                pattern = f"**/*{file_type}"
                for file_path in sorted(dir_path.glob(pattern)):
                    path_str = str(file_path)
                    if any(skip in path_str for skip in [
                        "__pycache__", ".ipynb_checkpoints", "node_modules", ".git"
                    ]):
                        continue
                    chunks = self.process_file(file_path, incremental=incremental)
                    all_chunks.extend(chunks)

        elapsed = (datetime.now() - start_time).total_seconds()
        self._stats["processing_time"] = elapsed
        self._stats["total_chunks"] = len(all_chunks)
        self._stats["total_tokens"] = sum(c.token_estimate for c in all_chunks)

        logger.info(
            "Processados %d arquivos (%d cache), %d chunks, %.1fs",
            self._stats["files_processed"] + self._stats["files_from_cache"],
            self._stats["files_from_cache"],
            len(all_chunks),
            elapsed,
        )
        return all_chunks

    def process_file(self, file_path: Path, incremental: bool = True) -> list[Chunk]:
        """Processa um unico arquivo.

        Args:
            file_path: Caminho do arquivo.
            incremental: Se True, usa cache.

        Returns:
            Lista de chunks do arquivo.
        """
        file_path = Path(file_path)

        if incremental and self._is_cached(file_path):
            chunks = self._load_cache(file_path)
            self._stats["files_from_cache"] += 1
            for c in chunks:
                self._stats["chunks_by_type"][c.chunk_type.value] += 1
            return chunks

        parser = self._registry.get_parser(file_path)
        if parser is None:
            logger.warning("Sem parser para: %s", file_path.suffix)
            self._stats["files_skipped"] += 1
            return []

        try:
            chunks = parser.parse(file_path)
        except Exception as e:
            logger.error("Erro ao parsear %s: %s", file_path, e)
            self._stats["files_skipped"] += 1
            return []

        if file_path.exists():
            self._save_cache(file_path, chunks)
        self._stats["files_processed"] += 1

        for c in chunks:
            self._stats["chunks_by_type"][c.chunk_type.value] += 1

        logger.debug(
            "Parsed %s: %d chunks (%d tokens)",
            file_path.name,
            len(chunks),
            sum(c.token_estimate for c in chunks),
        )
        return chunks

    def get_stats(self) -> dict:
        return {
            "files_processed": self._stats["files_processed"],
            "files_from_cache": self._stats["files_from_cache"],
            "files_skipped": self._stats["files_skipped"],
            "total_chunks": self._stats["total_chunks"],
            "total_tokens": self._stats["total_tokens"],
            "chunks_by_type": dict(self._stats["chunks_by_type"]),
            "processing_time": self._stats["processing_time"],
        }

    def clear_cache(self) -> None:
        count = 0
        for cache_file in self._cache_dir.glob("*.json"):
            cache_file.unlink()
            count += 1
        logger.info("Cache limpo: %d arquivos de %s", count, self._cache_dir)

    # --- Cache privado ---

    def _cache_path_for(self, file_path: Path) -> Path:
        key = str(file_path.resolve())
        name_hash = hashlib.sha256(key.encode()).hexdigest()[:16]
        safe_name = file_path.stem.replace(" ", "_")
        return self._cache_dir / f"{safe_name}_{name_hash}.json"

    def _is_cached(self, file_path: Path) -> bool:
        cache_path = self._cache_path_for(file_path)
        if not cache_path.exists():
            return False
        try:
            with open(cache_path, encoding="utf-8") as f:
                cache_data = json.load(f)
            cached_mtime = cache_data.get("mtime", 0)
            current_mtime = file_path.stat().st_mtime
            return current_mtime <= cached_mtime
        except (json.JSONDecodeError, OSError) as e:
            logger.debug("Cache check falhou para %s: %s", file_path, e)
            return False

    def _load_cache(self, file_path: Path) -> list[Chunk]:
        cache_path = self._cache_path_for(file_path)
        try:
            with open(cache_path, encoding="utf-8") as f:
                cache_data = json.load(f)
            chunks = []
            for c in cache_data.get("chunks", []):
                chunks.append(Chunk(
                    chunk_id=c["chunk_id"],
                    content=c["content"],
                    chunk_type=c["chunk_type"],
                    source_file=c["source_file"],
                    metadata=c.get("metadata", {}),
                ))
            return chunks
        except (json.JSONDecodeError, OSError, KeyError) as e:
            logger.warning("Falha ao carregar cache para %s: %s", file_path, e)
            return []

    def _save_cache(self, file_path: Path, chunks: list[Chunk]) -> None:
        cache_path = self._cache_path_for(file_path)
        try:
            content_bytes = file_path.read_bytes()
            file_hash = hashlib.sha256(content_bytes).hexdigest()
        except OSError:
            file_hash = ""

        cache_data = {
            "source_file": str(file_path.resolve()),
            "mtime": file_path.stat().st_mtime,
            "file_hash": file_hash,
            "processed_at": datetime.now().isoformat(),
            "chunks": [
                {
                    "chunk_id": c.chunk_id,
                    "content": c.content,
                    "chunk_type": c.chunk_type.value if hasattr(c.chunk_type, "value") else c.chunk_type,
                    "source_file": c.source_file,
                    "metadata": c.metadata,
                }
                for c in chunks
            ],
        }

        try:
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)
        except OSError as e:
            logger.warning("Falha ao salvar cache para %s: %s", file_path, e)
