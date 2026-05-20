"""Ollama adapter — talks to a local Ollama daemon over HTTP.

Targets the ``/api/chat`` endpoint (non-streaming). The default ``base_url``
is ``http://localhost:11434``. No API key required.
"""
from __future__ import annotations

from typing import Any

import httpx

from graphenda_build.llm.base import LLMError, LLMMessage, LLMProvider


class OllamaLLMProvider(LLMProvider):
    """Ollama local-LLM provider."""

    name = "ollama"

    DEFAULT_BASE_URL = "http://localhost:11434"
    DEFAULT_MODEL = "llama3.1:8b"

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
            base_url=base_url or self.DEFAULT_BASE_URL,
            model=model or self.DEFAULT_MODEL,
            timeout=timeout,
            **extra,
        )
        self._client = httpx.Client(timeout=timeout, base_url=self.base_url)

    def close(self) -> None:
        self._client.close()

    def __del__(self) -> None:
        try:
            self._client.close()
        except Exception:
            pass

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

        options: dict[str, Any] = {
            "temperature": temperature,
            "num_predict": max_tokens,
        }
        for k in ("top_p", "top_k", "repeat_penalty"):
            if k in kwargs:
                options[k] = kwargs[k]

        payload: dict[str, Any] = {
            "model": model or self.model,
            "messages": api_messages,
            "stream": False,
            "options": options,
        }

        try:
            resp = self._client.post("/api/chat", json=payload)
        except httpx.HTTPError as exc:
            raise LLMError(f"Ollama network error: {exc}") from exc

        if resp.status_code >= 400:
            raise LLMError(f"Ollama HTTP {resp.status_code}: {resp.text[:200]}")

        try:
            body = resp.json()
        except ValueError as exc:
            raise LLMError(f"Ollama returned non-JSON: {exc}") from exc

        message = body.get("message") if isinstance(body, dict) else None
        if not isinstance(message, dict):
            raise LLMError(f"Ollama response missing 'message': {body!r}")
        content = message.get("content", "")
        return content if isinstance(content, str) else str(content)
