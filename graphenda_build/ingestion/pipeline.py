"""Pipeline de ingestao generico para a Graphenda Engine.

Orchestrates 4 estagios: Discovery & Chunking → Triple Extraction →
Entity Resolution → Graph Loading.
Parametrizado pela ontologia ativa — trocar YAML muda o que e extraido.
Suporta incremental ingestion via SHA-256 manifest.
"""
import hashlib
import json
import logging
import time
from pathlib import Path

from graphenda_build.ontology.manager import OntologySchema
from graphenda_build.ingestion.chunker import Chunker
from graphenda_build.ingestion.entity_resolver import EntityResolver, ResolvedTriple
from graphenda_build.ingestion.parsers.registry import ParserRegistry
from graphenda_build.ingestion.triple_extractor import OntologyTripleExtractor
from graphenda_shared.graph.connection import Neo4jConnection

logger = logging.getLogger(__name__)

CACHE_DIR = Path("cache")
MANIFEST_PATH = CACHE_DIR / "pipeline_manifest.json"


class IngestPipeline:
    """Pipeline de ingestao ontology-aware.

    Aceita OntologySchema como parametro e orquestra:
    1. Discovery & Chunking (via ParserRegistry)
    2. Triple Extraction (via LLM com ontologia injetada)
    3. Entity Resolution (via aliases da ontologia)
    4. Graph Loading (extensivel — loader nao incluido no MVP)
    """

    def __init__(
        self,
        ontology: OntologySchema,
        neo4j: Neo4jConnection | None = None,
        registry: ParserRegistry | None = None,
        api_key: str | None = None,
        model: str = "claude-sonnet-4-20250514",
        batch_size: int = 50,
    ) -> None:
        """Inicializa pipeline com ontologia.

        Args:
            ontology: Schema da ontologia ativa.
            neo4j: Conexao Neo4j para graph loading (opcional — se None, retorna triples sem carregar).
            registry: ParserRegistry customizado (opcional).
            api_key: Anthropic API key (opcional, usa env var se None).
            model: Modelo LLM para extracao.
            batch_size: Tamanho padrao do batch.
        """
        self._ontology = ontology
        self._neo4j = neo4j
        self._batch_size = batch_size

        self._registry = registry or ParserRegistry.default()
        self._chunker = Chunker(registry=self._registry)
        self._extractor = OntologyTripleExtractor(
            ontology=ontology, model=model, api_key=api_key,
        )
        self._resolver = EntityResolver(ontology=ontology)

        self._stats: dict = {}
        self._step_times: dict = {}
        self._resolved_triples: list[ResolvedTriple] = []

    @property
    def ontology(self) -> OntologySchema:
        return self._ontology

    def run(
        self,
        source_dirs: list[dict],
        incremental: bool = True,
        dry_run: bool = False,
        batch_size: int | None = None,
    ) -> dict:
        """Executa o pipeline completo.

        Args:
            source_dirs: Diretorios fonte. Cada dict tem 'path' e 'file_types'.
            incremental: Se True, pula arquivos inalterados.
            dry_run: Se True, extrai triples mas nao carrega no graph.
            batch_size: Override do batch size padrao.

        Returns:
            Dict com estatisticas do pipeline.
        """
        batch_size = batch_size or self._batch_size
        total_start = time.time()

        self._stats = {
            "mode": "incremental" if incremental else "full",
            "dry_run": dry_run,
            "ontology": self._ontology.name,
            "source_dirs": len(source_dirs),
            "files_found": 0,
            "files_skipped": 0,
            "files_processed": 0,
            "chunks_created": 0,
            "triples_extracted": 0,
            "triples_resolved": 0,
            "errors": [],
        }

        logger.info(
            "Pipeline iniciado: ontologia=%s, mode=%s, dry_run=%s, batch=%d",
            self._ontology.name, self._stats["mode"], dry_run, batch_size,
        )

        # Carregar manifest para modo incremental
        manifest = self._load_manifest() if incremental else {}

        # Etapa 1: Discovery & Chunking
        step_start = time.time()
        files = self._discover_files(source_dirs)
        self._stats["files_found"] = len(files)

        if incremental:
            files, skipped = self._filter_unchanged(files, manifest)
            self._stats["files_skipped"] = skipped
            logger.info(
                "Incremental: %d a processar, %d pulados", len(files), skipped
            )
        self._step_times["discover"] = time.time() - step_start

        if not files:
            logger.info("Nenhum arquivo para processar.")
            self._stats["total_time"] = time.time() - total_start
            return self._stats

        # Etapa 2: Chunking
        step_start = time.time()
        all_chunks = []
        for file_info in files:
            try:
                chunks = self._chunker.process_file(
                    Path(file_info["path"]), incremental=False
                )
                all_chunks.extend(chunks)
                logger.info("Chunked %s: %d chunks", file_info["path"], len(chunks))
            except Exception as e:
                error_msg = f"Chunking falhou para {file_info['path']}: {e}"
                logger.warning(error_msg)
                self._stats["errors"].append(error_msg)

        self._stats["chunks_created"] = len(all_chunks)
        self._step_times["chunk"] = time.time() - step_start

        # Etapa 3: Triple Extraction
        step_start = time.time()
        all_triples = []

        if not dry_run:
            for i in range(0, len(all_chunks), batch_size):
                batch = all_chunks[i : i + batch_size]
                try:
                    triples = self._extractor.extract_batch(batch, batch_size=batch_size)
                    all_triples.extend(triples)
                except Exception as e:
                    error_msg = f"Extracao falhou para batch {i}: {e}"
                    logger.warning(error_msg)
                    self._stats["errors"].append(error_msg)

        self._stats["triples_extracted"] = len(all_triples)
        self._step_times["extract"] = time.time() - step_start

        # Etapa 4: Entity Resolution
        step_start = time.time()
        resolved_triples: list[ResolvedTriple] = []

        if all_triples:
            try:
                resolver_triples = [
                    ResolvedTriple(
                        subject=t.subject.name,
                        predicate=t.predicate,
                        object=t.object.name,
                        subject_type=t.subject.type,
                        object_type=t.object.type,
                        source_chunk_id=t.source_chunk or "",
                        confidence=t.confidence,
                    )
                    for t in all_triples
                ]
                resolved_triples = self._resolver.resolve_triples(resolver_triples)
            except Exception as e:
                error_msg = f"Entity resolution falhou: {e}"
                logger.error(error_msg)
                self._stats["errors"].append(error_msg)

        self._stats["triples_resolved"] = len(resolved_triples)
        self._resolved_triples = resolved_triples
        self._step_times["resolve"] = time.time() - step_start

        # Etapa 5: Graph Loading
        step_start = time.time()
        if resolved_triples and self._neo4j and not dry_run:
            try:
                loaded = self._load_to_graph(resolved_triples)
                self._stats["entities_loaded"] = loaded["entities"]
                self._stats["relationships_loaded"] = loaded["relationships"]
            except Exception as e:
                error_msg = f"Graph loading falhou: {e}"
                logger.error(error_msg)
                self._stats["errors"].append(error_msg)
        else:
            self._stats["entities_loaded"] = 0
            self._stats["relationships_loaded"] = 0
        self._step_times["load"] = time.time() - step_start

        # Atualizar manifest
        self._update_manifest(manifest, files)

        self._stats["total_time"] = time.time() - total_start
        self._stats["files_processed"] = len(files)
        self._stats["step_times"] = self._step_times

        logger.info(
            "Pipeline completo em %.1fs: %d arquivos, %d chunks, %d triples",
            self._stats["total_time"],
            self._stats["files_processed"],
            self._stats["chunks_created"],
            self._stats["triples_resolved"],
        )

        return self._stats

    def run_step(self, step: str, **kwargs) -> dict:
        """Executa um unico estagio para debug.

        Args:
            step: Um de 'chunk', 'extract', 'resolve'.
            **kwargs: Argumentos especificos do estagio.

        Returns:
            Resultado do estagio com dados e timing.
        """
        valid_steps = ("chunk", "extract", "resolve")
        if step not in valid_steps:
            raise ValueError(f"Estagio invalido '{step}'. Use: {valid_steps}")

        start = time.time()
        result: dict = {"step": step}

        if step == "chunk":
            source_dirs = kwargs.get("source_dirs", [])
            chunks = self._chunker.process_sources(source_dirs, incremental=False)
            result["chunks"] = chunks
            result["count"] = len(chunks)

        elif step == "extract":
            chunks = kwargs.get("chunks", [])
            triples = self._extractor.extract_batch(chunks)
            result["triples"] = triples
            result["count"] = len(triples)

        elif step == "resolve":
            triples = kwargs.get("triples", [])
            resolved = self._resolver.resolve_triples(triples)
            result["triples"] = resolved
            result["count"] = len(resolved)

        result["time"] = time.time() - start
        return result

    def get_report(self) -> str:
        """Gera relatorio legivel do pipeline."""
        if not self._stats:
            return "Nenhum pipeline executado."

        lines = [
            "=" * 60,
            "  GRAPHENDA INGESTION PIPELINE REPORT",
            "=" * 60,
            "",
            f"  Ontologia:       {self._stats.get('ontology', 'N/A')}",
            f"  Mode:            {self._stats.get('mode', 'N/A')}",
            f"  Dry Run:         {self._stats.get('dry_run', False)}",
            "",
            "  FILES",
            f"    Found:         {self._stats.get('files_found', 0)}",
            f"    Skipped:       {self._stats.get('files_skipped', 0)}",
            f"    Processed:     {self._stats.get('files_processed', 0)}",
            "",
            "  PIPELINE OUTPUT",
            f"    Chunks:        {self._stats.get('chunks_created', 0)}",
            f"    Triples (raw): {self._stats.get('triples_extracted', 0)}",
            f"    Triples (res): {self._stats.get('triples_resolved', 0)}",
            "",
            "  GRAPH LOADING",
            f"    Entities:      {self._stats.get('entities_loaded', 0)}",
            f"    Relationships: {self._stats.get('relationships_loaded', 0)}",
            "",
        ]

        step_times = self._stats.get("step_times", {})
        if step_times:
            lines.append("  STEP TIMINGS")
            for step_name, elapsed in step_times.items():
                lines.append(f"    {step_name:<14} {elapsed:.1f}s")
            lines.append("")

        errors = self._stats.get("errors", [])
        if errors:
            lines.append(f"  ERRORS ({len(errors)})")
            for err in errors[:10]:
                lines.append(f"    - {err}")
            lines.append("")

        total = self._stats.get("total_time", 0)
        lines.append(f"  TOTAL TIME:      {total:.1f}s ({total / 60:.1f}min)")
        lines.append("=" * 60)

        return "\n".join(lines)

    def get_triples(self) -> list[ResolvedTriple]:
        """Retorna os triples resolvidos do ultimo pipeline run."""
        return self._resolved_triples

    # --- Graph Loading ---

    def _load_to_graph(self, triples: list[ResolvedTriple]) -> dict[str, int]:
        """Carrega triples resolvidos no Neo4j.

        Converte ResolvedTriple em Entity/Relationship e usa GraphLoader.

        Args:
            triples: Lista de triples resolvidos.

        Returns:
            Dict com contagem de entities e relationships carregados.
        """
        from graphenda_shared.models.core import Entity, Relationship
        from graphenda_build.graph.loader import GraphLoader

        loader = GraphLoader(conn=self._neo4j, ontology=self._ontology)

        # Extrair entidades unicas dos triples
        seen_entities: dict[str, Entity] = {}
        relationships: list[Relationship] = []

        for triple in triples:
            # Subject
            if triple.subject not in seen_entities:
                seen_entities[triple.subject] = Entity(
                    name=triple.subject,
                    type=triple.subject_type,
                )
            # Object
            if triple.object not in seen_entities:
                seen_entities[triple.object] = Entity(
                    name=triple.object,
                    type=triple.object_type,
                )
            # Relationship
            relationships.append(Relationship(
                source=triple.subject,
                relation=triple.predicate,
                target=triple.object,
                properties={"confidence": triple.confidence},
            ))

        entities = list(seen_entities.values())
        n_ent = loader.load_entities(entities)
        n_rel = loader.load_relationships(relationships)

        logger.info(
            "Graph loading: %d entities, %d relationships loaded",
            n_ent, n_rel,
        )
        return {"entities": n_ent, "relationships": n_rel}

    # --- Helpers privados ---

    def _discover_files(self, source_dirs: list[dict]) -> list[dict]:
        files: list[dict] = []
        for source in source_dirs:
            dir_path = Path(source["path"])
            if not dir_path.exists():
                logger.warning("Diretorio nao encontrado: %s", dir_path)
                continue

            for file_type in source.get("file_types", [".py"]):
                pattern = f"**/*{file_type}"
                for file_path in sorted(dir_path.glob(pattern)):
                    path_str = str(file_path)
                    if any(skip in path_str for skip in [
                        "__pycache__", ".ipynb_checkpoints", "node_modules", ".git"
                    ]):
                        continue
                    file_hash = self._hash_file(file_path)
                    files.append({
                        "path": str(file_path),
                        "file_type": file_type,
                        "hash": file_hash,
                    })
        return files

    def _filter_unchanged(
        self, files: list[dict], manifest: dict
    ) -> tuple[list[dict], int]:
        changed: list[dict] = []
        skipped = 0
        for file_info in files:
            previous_hash = manifest.get(file_info["path"])
            if previous_hash and previous_hash == file_info["hash"]:
                skipped += 1
            else:
                changed.append(file_info)
        return changed, skipped

    @staticmethod
    def _hash_file(file_path: Path) -> str:
        try:
            content = file_path.read_bytes()
            return hashlib.sha256(content).hexdigest()[:16]
        except Exception:
            return ""

    def _load_manifest(self) -> dict:
        if MANIFEST_PATH.exists():
            try:
                with open(MANIFEST_PATH, encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.warning("Manifest nao carregado: %s", e)
        return {}

    def _update_manifest(self, manifest: dict, files: list[dict]) -> None:
        for file_info in files:
            manifest[file_info["path"]] = file_info["hash"]

        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        try:
            with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)
        except IOError as e:
            logger.warning("Manifest nao salvo: %s", e)
