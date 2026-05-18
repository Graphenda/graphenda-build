"""Extrator de triples ontology-aware usando LLM.

Injeta entity types e relationship types da ontologia ativa nos prompts.
Suporta chamadas individuais e batch com cache por chunk.
Implementa BaseTripleExtractor.
"""
import json
import logging
import re
from pathlib import Path

from graphenda_build.core.base_extractor import BaseTripleExtractor
from graphenda_shared.models.core import Chunk, Entity, Triple
from graphenda_build.ontology.manager import OntologySchema
from graphenda_build.ingestion.prompts import (
    build_few_shot_messages,
    build_system_prompt,
    build_user_prompt,
)

logger = logging.getLogger(__name__)


class OntologyTripleExtractor(BaseTripleExtractor):
    """Extrai triples de chunks usando LLM com ontologia injetada.

    A ontologia define quais entity types e relationship types sao validos.
    Prompts sao construidos dinamicamente a partir do schema.
    """

    def __init__(
        self,
        ontology: OntologySchema,
        model: str = "claude-sonnet-4-20250514",
        api_key: str | None = None,
        cache_dir: str | Path = "cache/triples",
    ) -> None:
        self._ontology = ontology
        self._model = model
        self._api_key = api_key
        self._cache_dir = Path(cache_dir)
        self._cache_dir.mkdir(parents=True, exist_ok=True)

        # Prompts construidos a partir da ontologia
        self._system_prompt = build_system_prompt(ontology)
        self._few_shot_messages = build_few_shot_messages(ontology)
        self._valid_entity_types = set(ontology.entity_type_names)
        self._valid_relation_types = set(ontology.relationship_type_names)

    def extract(self, chunks: list[Chunk], ontology: OntologySchema) -> list[Triple]:
        """Extrai triples de uma lista de chunks.

        Args:
            chunks: Lista de chunks a processar.
            ontology: Schema da ontologia (pode atualizar em runtime).

        Returns:
            Lista de Triple extraidos e validados.
        """
        # Atualiza ontologia se diferente
        if ontology.name != self._ontology.name:
            self._update_ontology(ontology)

        all_triples: list[Triple] = []
        for chunk in chunks:
            cached = self._load_cache(chunk.chunk_id)
            if cached is not None:
                all_triples.extend(cached)
                continue

            triples = self.extract_from_chunk(chunk)
            all_triples.extend(triples)

        logger.info("Extraidos %d triples de %d chunks", len(all_triples), len(chunks))
        return all_triples

    def extract_from_chunk(self, chunk: Chunk) -> list[Triple]:
        """Extrai triples de um unico chunk via API.

        Args:
            chunk: Chunk a processar.

        Returns:
            Lista de Triple validados.
        """
        cached = self._load_cache(chunk.chunk_id)
        if cached is not None:
            return cached

        user_prompt = self._build_chunk_prompt(chunk)
        messages = self._few_shot_messages + [
            {"role": "user", "content": user_prompt},
        ]

        try:
            from anthropic import Anthropic

            client = Anthropic(api_key=self._api_key) if self._api_key else Anthropic()
            response = client.messages.create(
                model=self._model,
                max_tokens=2048,
                system=self._system_prompt,
                messages=messages,
            )
            response_text = response.content[0].text
        except Exception as e:
            logger.error("API call falhou para chunk %s: %s", chunk.chunk_id, e)
            return []

        triples = self._parse_response(response_text, chunk)
        self._save_cache(chunk.chunk_id, triples)

        logger.info(
            "Extraidos %d triples do chunk %s (%s)",
            len(triples), chunk.chunk_id, chunk.metadata.get("name", "?"),
        )
        return triples

    def extract_batch(self, chunks: list[Chunk], batch_size: int = 50) -> list[Triple]:
        """Extrai triples em batch (com fallback individual).

        Args:
            chunks: Chunks a processar.
            batch_size: Tamanho do batch para API.

        Returns:
            Lista de todos os triples extraidos.
        """
        all_triples: list[Triple] = []
        uncached: list[Chunk] = []

        for chunk in chunks:
            cached = self._load_cache(chunk.chunk_id)
            if cached is not None:
                all_triples.extend(cached)
            else:
                uncached.append(chunk)

        if not uncached:
            logger.info("Todos os %d chunks ja estao em cache", len(chunks))
            return all_triples

        logger.info(
            "Processando %d chunks nao-cacheados (%d em cache)",
            len(uncached), len(chunks) - len(uncached),
        )

        # Processa em batches via API individual (batch API pode ser adicionada depois)
        for i in range(0, len(uncached), batch_size):
            batch = uncached[i : i + batch_size]
            for chunk in batch:
                triples = self.extract_from_chunk(chunk)
                all_triples.extend(triples)

        return all_triples

    # --- Privados ---

    def _update_ontology(self, ontology: OntologySchema) -> None:
        self._ontology = ontology
        self._system_prompt = build_system_prompt(ontology)
        self._few_shot_messages = build_few_shot_messages(ontology)
        self._valid_entity_types = set(ontology.entity_type_names)
        self._valid_relation_types = set(ontology.relationship_type_names)

    def _build_chunk_prompt(self, chunk: Chunk) -> str:
        context_parts: list[str] = []
        if chunk.metadata.get("module_path"):
            context_parts.append(f"Module: {chunk.metadata['module_path']}")
        if chunk.metadata.get("document_title"):
            context_parts.append(f"Document: {chunk.metadata['document_title']}")
        if chunk.metadata.get("notebook"):
            context_parts.append(f"Notebook: {chunk.metadata['notebook']}")

        return build_user_prompt(
            content=chunk.content,
            chunk_type=chunk.chunk_type.value,
            source_file=chunk.source_file,
            context=" | ".join(context_parts) if context_parts else "",
        )

    def _parse_response(self, response_text: str, chunk: Chunk) -> list[Triple]:
        """Parseia resposta JSON em Triple objects validados contra a ontologia."""
        try:
            data = json.loads(response_text)
        except json.JSONDecodeError:
            match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", response_text, re.DOTALL)
            if match:
                try:
                    data = json.loads(match.group(1))
                except json.JSONDecodeError:
                    logger.warning("JSON invalido do chunk %s", chunk.chunk_id)
                    return []
            else:
                logger.warning("JSON invalido do chunk %s", chunk.chunk_id)
                return []

        raw_triples = data.get("triples", [])
        validated: list[Triple] = []

        for raw in raw_triples:
            try:
                subject = raw["subject"]
                predicate = raw["predicate"]
                obj = raw["object"]

                if subject["type"] not in self._valid_entity_types:
                    logger.debug("Tipo de subject invalido: '%s'", subject["type"])
                    continue
                if obj["type"] not in self._valid_entity_types:
                    logger.debug("Tipo de object invalido: '%s'", obj["type"])
                    continue
                if predicate not in self._valid_relation_types:
                    logger.debug("Predicado invalido: '%s'", predicate)
                    continue

                triple = Triple(
                    subject=Entity(name=subject["name"], type=subject["type"]),
                    predicate=predicate,
                    object=Entity(name=obj["name"], type=obj["type"]),
                    confidence=float(raw.get("confidence", 0.0)),
                    source_chunk=chunk.chunk_id,
                )
                validated.append(triple)

            except (KeyError, TypeError, ValueError) as e:
                logger.debug("Triple malformado: %s", e)
                continue

        logger.debug(
            "Parseados %d/%d triples do chunk %s",
            len(validated), len(raw_triples), chunk.chunk_id,
        )
        return validated

    def _save_cache(self, chunk_id: str, triples: list[Triple]) -> None:
        cache_path = self._cache_dir / f"{chunk_id}.json"
        data = {
            "chunk_id": chunk_id,
            "n_triples": len(triples),
            "triples": [t.model_dump() for t in triples],
        }
        cache_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    def _load_cache(self, chunk_id: str) -> list[Triple] | None:
        cache_path = self._cache_dir / f"{chunk_id}.json"
        if not cache_path.exists():
            return None
        try:
            data = json.loads(cache_path.read_text())
            return [Triple.model_validate(t) for t in data["triples"]]
        except (json.JSONDecodeError, KeyError) as e:
            logger.warning("Cache corrompido para chunk %s: %s", chunk_id, e)
            return None
