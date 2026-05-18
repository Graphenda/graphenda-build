"""Parser de arquivos Python usando AST para chunking semantico.

Extrai classes e funcoes top-level como chunks individuais,
preservando codigo-fonte, docstrings e metadados estruturais.
"""
import ast
import hashlib
import logging
from pathlib import Path

from graphenda_build.core.base_parser import BaseDocumentParser
from graphenda_shared.models.core import Chunk, ChunkType

logger = logging.getLogger(__name__)


class PythonDocumentParser(BaseDocumentParser):
    """Parser de .py via AST — domain-agnostic."""

    def supported_extensions(self) -> list[str]:
        return [".py"]

    def parse(self, file_path: Path) -> list[Chunk]:
        file_path = Path(file_path)
        if not file_path.exists():
            logger.warning("Arquivo nao encontrado: %s", file_path)
            return []

        try:
            source = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            logger.warning("Erro de decode: %s", file_path)
            return []

        try:
            tree = ast.parse(source, filename=str(file_path))
        except SyntaxError as e:
            logger.warning("Erro de sintaxe em %s: %s", file_path, e)
            return []

        chunks: list[Chunk] = []
        module_path = self._file_to_module(file_path)

        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.ClassDef):
                chunk = self._extract_class(node, source, file_path, module_path)
                if chunk:
                    chunks.append(chunk)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                chunk = self._extract_function(node, source, file_path, module_path)
                if chunk:
                    chunks.append(chunk)

        # Fallback: docstring do modulo
        if not chunks and source.strip():
            module_doc = ast.get_docstring(tree)
            if module_doc:
                chunks.append(Chunk(
                    chunk_id=self._make_id(file_path, "module"),
                    content=module_doc,
                    chunk_type=ChunkType.PYTHON_MODULE,
                    source_file=str(file_path),
                    metadata={
                        "name": file_path.stem,
                        "module_path": module_path,
                        "type": "module_docstring",
                    },
                ))

        logger.debug("Parsed %s: %d chunks", file_path.name, len(chunks))
        return chunks

    # --- Extracoes privadas ---

    def _extract_class(
        self, node: ast.ClassDef, source: str, file_path: Path, module_path: str
    ) -> Chunk | None:
        class_source = ast.get_source_segment(source, node)
        if not class_source:
            return None

        docstring = ast.get_docstring(node) or ""
        methods = [
            item.name
            for item in node.body
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        bases = []
        for base in node.bases:
            if isinstance(base, ast.Name):
                bases.append(base.id)
            elif isinstance(base, ast.Attribute):
                bases.append(ast.unparse(base))

        init_params = self._extract_init_params(node)
        decorators = [ast.unparse(d) for d in node.decorator_list]

        return Chunk(
            chunk_id=self._make_id(file_path, node.name),
            content=class_source,
            chunk_type=ChunkType.PYTHON_CLASS,
            source_file=str(file_path),
            metadata={
                "name": node.name,
                "module_path": f"{module_path}.{node.name}",
                "bases": bases,
                "methods": methods,
                "init_params": init_params,
                "docstring": docstring[:500],
                "decorators": decorators,
                "line_start": node.lineno,
                "line_end": node.end_lineno or node.lineno,
            },
        )

    def _extract_function(
        self,
        node: ast.FunctionDef | ast.AsyncFunctionDef,
        source: str,
        file_path: Path,
        module_path: str,
    ) -> Chunk | None:
        if node.name.startswith("_") and node.name != "__init__":
            return None

        func_source = ast.get_source_segment(source, node)
        if not func_source:
            return None

        docstring = ast.get_docstring(node) or ""
        params = self._extract_function_params(node)
        decorators = [ast.unparse(d) for d in node.decorator_list]

        return Chunk(
            chunk_id=self._make_id(file_path, node.name),
            content=func_source,
            chunk_type=ChunkType.PYTHON_FUNCTION,
            source_file=str(file_path),
            metadata={
                "name": node.name,
                "module_path": f"{module_path}.{node.name}",
                "params": params,
                "docstring": docstring[:500],
                "decorators": decorators,
                "is_async": isinstance(node, ast.AsyncFunctionDef),
                "line_start": node.lineno,
                "line_end": node.end_lineno or node.lineno,
            },
        )

    def _extract_init_params(self, class_node: ast.ClassDef) -> list[dict]:
        for item in class_node.body:
            if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                return self._extract_function_params(item)
        return []

    def _extract_function_params(self, func_node: ast.FunctionDef) -> list[dict]:
        params: list[dict] = []
        args = func_node.args

        all_args = list(args.args) + list(args.posonlyargs) + list(args.kwonlyargs)
        defaults = [None] * (len(args.args) - len(args.defaults)) + list(args.defaults)
        kw_defaults = list(args.kw_defaults)

        for i, arg in enumerate(all_args):
            if arg.arg in ("self", "cls"):
                continue
            param: dict = {"name": arg.arg}
            if arg.annotation:
                try:
                    param["type"] = ast.unparse(arg.annotation)
                except Exception:
                    pass
            if i < len(defaults) and defaults[i] is not None:
                try:
                    param["default"] = ast.unparse(defaults[i])
                except Exception:
                    pass
            elif i >= len(args.args) and (i - len(args.args)) < len(kw_defaults):
                kw_idx = i - len(args.args)
                if kw_defaults[kw_idx] is not None:
                    try:
                        param["default"] = ast.unparse(kw_defaults[kw_idx])
                    except Exception:
                        pass
            params.append(param)

        return params

    def _file_to_module(self, file_path: Path) -> str:
        """Converte caminho de arquivo em modulo Python."""
        parts = file_path.resolve().parts
        # Encontra raiz do projeto (diretorio que contem graphenda_build/)
        for i, part in enumerate(parts):
            if part == "graphenda_build":
                module_parts = list(parts[i:])
                module_parts[-1] = module_parts[-1].replace(".py", "")
                if module_parts[-1] == "__init__":
                    module_parts = module_parts[:-1]
                return ".".join(module_parts)
        return file_path.stem

    @staticmethod
    def _make_id(file_path: Path, name: str) -> str:
        key = f"{file_path}::{name}"
        return hashlib.sha256(key.encode()).hexdigest()[:16]
