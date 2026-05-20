"""LLM provider abstraction for graphenda-build.

Two call sites in the library need an LLM: triple extraction and community
summarization. Both share the same primitive (`system + messages -> text`),
so this package exposes one synchronous `LLMProvider` interface and a small
set of adapters that implement it.

Public surface:
    LLMProvider, LLMMessage, LLMError, build_provider, list_provider_names,
    provider_from_env.
"""
from graphenda_build.llm.base import (
    LLMError,
    LLMMessage,
    LLMProvider,
)
from graphenda_build.llm.registry import (
    OPENAI_COMPATIBLE_PRESETS,
    build_provider,
    list_provider_names,
    provider_from_env,
)

__all__ = [
    "LLMError",
    "LLMMessage",
    "LLMProvider",
    "OPENAI_COMPATIBLE_PRESETS",
    "build_provider",
    "list_provider_names",
    "provider_from_env",
]
