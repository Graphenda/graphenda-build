"""OpenAI-compatible adapter — covers OpenAI itself and any vendor that
exposes a ``/v1/chat/completions`` route (DeepSeek, Groq, OpenRouter,
LM Studio, vLLM, …).

Different vendors are selected through :data:`OPENAI_COMPATIBLE_PRESETS` in
``registry.py`` — the only thing that changes is ``base_url``.
"""
from __future__ import annotations

from typing import Any

from graphenda_build.llm.base import LLMError, LLMMessage, LLMProvider


class OpenAILLMProvider(LLMProvider):
    """OpenAI-compatible Chat Completions provider."""

    name = "openai"

    DEFAULT_MODEL = "gpt-4o-mini"

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
        timeout: float = 120.0,
        **extra: Any,
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            model=model or self.DEFAULT_MODEL,
            timeout=timeout,
            **extra,
        )
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise LLMError(
                "openai SDK is not installed. Install with: pip install openai"
            ) from exc

        kwargs: dict[str, Any] = {"timeout": timeout}
        if api_key:
            kwargs["api_key"] = api_key
        if base_url:
            kwargs["base_url"] = base_url
        self._client = OpenAI(**kwargs)

    def complete(
        self,
        messages: list[LLMMessage],
        system: str | None = None,
        model: str | None = None,
        max_tokens: int = 2048,
        temperature: float = 0.3,
        **kwargs: Any,
    ) -> str:
        api_messages: list[dict[str, str]] = []
        if system:
            api_messages.append({"role": "system", "content": system})
        for m in messages:
            api_messages.append({"role": m.role, "content": m.content})

        call_kwargs: dict[str, Any] = {
            "model": model or self.model,
            "messages": api_messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        for k in ("top_p", "frequency_penalty", "presence_penalty", "stop"):
            if k in kwargs:
                call_kwargs[k] = kwargs[k]

        try:
            response = self._client.chat.completions.create(**call_kwargs)
        except Exception as exc:
            raise LLMError(f"OpenAI-compatible call failed: {exc}") from exc

        if not response.choices:
            raise LLMError("OpenAI-compatible response had no choices")
        text = response.choices[0].message.content
        return text or ""
