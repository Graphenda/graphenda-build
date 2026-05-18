"""Templates de extracao de triples ontology-aware.

Os prompts injetam entity types e relationship types da ontologia ativa,
tornando a extracao generica — trocar YAML muda o que e extraido.
"""
from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graphenda_build.ontology.manager import OntologySchema


# --- System Prompt Template ---

EXTRACTION_SYSTEM_PROMPT = """You are a knowledge graph extraction engine.

Your task is to extract (subject, predicate, object) triples from text chunks.
Each triple represents a relationship between two entities.

## Valid Entity Types
{entity_types}

## Valid Relation Types
{relation_types}

## Rules
1. Only use entity types and relation types from the lists above.
2. Entity names should be PascalCase for classes and snake_case for concepts/parameters.
3. Each triple must have a confidence score between 0.0 and 1.0.
4. Include evidence: a short quote or reference from the source text.
5. Do NOT invent entities that are not mentioned or clearly implied in the text.
6. Prefer specific entity names over generic ones.
7. A single chunk may produce 0 to 15 triples.

## Output Format
Respond with a JSON object containing a "triples" array. Each triple has:
- subject: {{"name": str, "type": str}}
- predicate: str (one of the valid relation types)
- object: {{"name": str, "type": str}}
- confidence: float (0.0 to 1.0)
- evidence: str (short excerpt from source)

If no triples can be extracted, return {{"triples": []}}.
""".strip()


# --- User Template ---

EXTRACTION_USER_TEMPLATE = """Extract knowledge triples from this {chunk_type} chunk.

Source: {source_file}
Context: {context}

---
{content}
---

Return a JSON object with a "triples" array. Only use valid entity and relation types.""".strip()


def build_system_prompt(ontology: OntologySchema) -> str:
    """Constroi system prompt injetando tipos da ontologia.

    Args:
        ontology: Schema da ontologia ativa.

    Returns:
        System prompt formatado.
    """
    entity_list = "\n".join(f"- {et}" for et in ontology.entity_type_names)
    relation_list = "\n".join(f"- {rt}" for rt in ontology.relationship_type_names)
    return EXTRACTION_SYSTEM_PROMPT.format(
        entity_types=entity_list,
        relation_types=relation_list,
    )


def build_user_prompt(
    content: str,
    chunk_type: str,
    source_file: str,
    context: str = "",
) -> str:
    """Constroi user prompt para um chunk especifico."""
    return EXTRACTION_USER_TEMPLATE.format(
        content=content,
        chunk_type=chunk_type,
        source_file=source_file,
        context=context or "Knowledge graph extraction",
    )


def build_few_shot_messages(ontology: OntologySchema) -> list[dict]:
    """Constroi exemplos few-shot baseados na ontologia ativa.

    Gera um exemplo generico que usa os entity types e relationship types
    reais da ontologia, para guiar o LLM.

    Args:
        ontology: Schema da ontologia ativa.

    Returns:
        Lista de dicts role/content para few-shot.
    """
    entity_types = ontology.entity_type_names
    rel_types = ontology.relationship_type_names

    # Exemplo generico usando os primeiros tipos disponiveis
    if len(entity_types) < 2 or not rel_types:
        return []

    et1 = entity_types[0]
    et2 = entity_types[1] if len(entity_types) > 1 else entity_types[0]
    rt = rel_types[0]

    example_input = build_user_prompt(
        content=(
            f"ExampleEntityA is a {et1} that relates to ExampleEntityB, "
            f"which is a {et2}. They are connected via {rt}."
        ),
        chunk_type="example",
        source_file="example.py",
    )

    example_output = {
        "triples": [
            {
                "subject": {"name": "ExampleEntityA", "type": et1},
                "predicate": rt,
                "object": {"name": "ExampleEntityB", "type": et2},
                "confidence": 0.90,
                "evidence": f"ExampleEntityA relates to ExampleEntityB via {rt}",
            }
        ]
    }

    return [
        {"role": "user", "content": example_input},
        {"role": "assistant", "content": json.dumps(example_output, indent=2)},
    ]
