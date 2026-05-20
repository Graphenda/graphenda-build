"""Provider lookup and construction by name.

Two flavors are registered:

- **Dedicated** adapters — each provider has its own class
  (Anthropic, Gemini, Ollama, internal-llm, internal-llm-agentic).
- **OpenAI-compatible** presets — all share :class:`OpenAIProvider`,
  differing only in ``base_url`` (openai, deepseek, groq, openrouter,
  lmstudio, vllm).

To pick a provider from process env, use :func:`provider_from_env` — that's
the entry point the CLI scripts use.
"""
from __future__ import annotations

import os
from typing import Any

from graphenda_build.llm.base import LLMError, LLMProvider


OPENAI_COMPATIBLE_PRESETS: dict[str, str | None] = {
    "openai": None,
    "deepseek": "https://api.deepseek.com/v1",
    "groq": "https://api.groq.com/openai/v1",
    "openrouter": "https://openrouter.ai/api/v1",
    "lmstudio": "http://localhost:1234/v1",
    "vllm": "http://localhost:8000/v1",
}


def _dedicated() -> dict[str, type[LLMProvider]]:
    """Imported lazily so optional SDKs aren't required just to import."""
    from graphenda_build.llm.anthropic import AnthropicLLMProvider
    from graphenda_build.llm.gemini import GeminiLLMProvider
    from graphenda_build.llm.internal_llm import InternalLLMProvider
    from graphenda_build.llm.internal_llm_agentic import (
        InternalLLMAgenticProvider,
    )
    from graphenda_build.llm.ollama import OllamaLLMProvider

    return {
        "anthropic": AnthropicLLMProvider,
        "gemini": GeminiLLMProvider,
        "internal-llm": InternalLLMProvider,
        "internal-llm-agentic": InternalLLMAgenticProvider,
        "ollama": OllamaLLMProvider,
    }


def list_provider_names() -> list[str]:
    """All known provider names, sorted."""
    return sorted(set(_dedicated()) | set(OPENAI_COMPATIBLE_PRESETS))


def build_provider(name: str, config: dict[str, Any] | None = None) -> LLMProvider:
    """Build a configured :class:`LLMProvider` by name.

    Lookup is case-insensitive. For OpenAI-compatible presets, the preset
    URL fills in ``base_url`` when the caller did not set one. An explicit
    ``base_url`` always wins.

    Args:
        name: Provider name. See :func:`list_provider_names`.
        config: Constructor kwargs (``api_key``, ``base_url``, ``model``,
            ``timeout``, and provider-specific extras like ``user_uuid``).

    Raises:
        LLMError: When ``name`` is not registered.
    """
    cfg = dict(config or {})
    key = name.lower()
    dedicated = _dedicated()

    if key in dedicated:
        return dedicated[key](**cfg)

    if key in OPENAI_COMPATIBLE_PRESETS:
        from graphenda_build.llm.openai import OpenAILLMProvider

        preset = OPENAI_COMPATIBLE_PRESETS[key]
        if preset and not cfg.get("base_url"):
            cfg["base_url"] = preset
        return OpenAILLMProvider(**cfg)

    raise LLMError(
        f"Unknown LLM provider: {name!r}. Known: {list_provider_names()}"
    )


def provider_from_env() -> LLMProvider:
    """Build the provider declared by environment variables.

    Reads ``GRAPHENDA_LLM_PROVIDER`` (default ``anthropic``) and then the
    per-provider env vars documented in ``.env.example``. Variables read:

    - ``GRAPHENDA_LLM_PROVIDER`` — provider name (default ``anthropic``)
    - ``GRAPHENDA_LLM_MODEL`` — default model id for the provider
    - ``GRAPHENDA_LLM_TIMEOUT`` — request timeout in seconds

    Provider-specific:

    - anthropic: ``ANTHROPIC_API_KEY``, ``ANTHROPIC_MODEL``
    - openai / deepseek / groq / openrouter / lmstudio / vllm:
      ``OPENAI_API_KEY``, ``OPENAI_BASE_URL``, ``OPENAI_MODEL``
    - gemini: ``GEMINI_API_KEY``, ``GEMINI_MODEL``
    - ollama: ``OLLAMA_BASE_URL`` (default ``http://localhost:11434``),
      ``OLLAMA_MODEL``
    - internal-llm / internal-llm-agentic: ``INTERNAL_LLM_ENDPOINT``,
      ``INTERNAL_LLM_USER_UUID``, ``INTERNAL_LLM_MODEL``
    """
    name = os.getenv("GRAPHENDA_LLM_PROVIDER", "anthropic").strip().lower()
    cfg: dict[str, Any] = {}

    timeout = os.getenv("GRAPHENDA_LLM_TIMEOUT")
    if timeout:
        cfg["timeout"] = float(timeout)

    generic_model = os.getenv("GRAPHENDA_LLM_MODEL")

    if name == "anthropic":
        cfg["api_key"] = os.getenv("ANTHROPIC_API_KEY") or None
        cfg["model"] = generic_model or os.getenv("ANTHROPIC_MODEL")
    elif name == "gemini":
        cfg["api_key"] = os.getenv("GEMINI_API_KEY") or None
        cfg["model"] = generic_model or os.getenv("GEMINI_MODEL")
    elif name == "ollama":
        cfg["base_url"] = (
            os.getenv("OLLAMA_BASE_URL") or "http://localhost:11434"
        )
        cfg["model"] = generic_model or os.getenv("OLLAMA_MODEL")
    elif name in {"internal-llm", "internal-llm-agentic"}:
        cfg["base_url"] = os.getenv("INTERNAL_LLM_ENDPOINT") or None
        cfg["user_uuid"] = os.getenv("INTERNAL_LLM_USER_UUID") or None
        cfg["model"] = generic_model or os.getenv("INTERNAL_LLM_MODEL")
    elif name in OPENAI_COMPATIBLE_PRESETS:
        cfg["api_key"] = os.getenv("OPENAI_API_KEY") or None
        explicit_base = os.getenv("OPENAI_BASE_URL")
        if explicit_base:
            cfg["base_url"] = explicit_base
        cfg["model"] = generic_model or os.getenv("OPENAI_MODEL")
    else:
        raise LLMError(
            f"Unknown LLM provider in GRAPHENDA_LLM_PROVIDER: {name!r}. "
            f"Known: {list_provider_names()}"
        )

    return build_provider(name, cfg)
