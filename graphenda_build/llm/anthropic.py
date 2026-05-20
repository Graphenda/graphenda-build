"""Anthropic adapter — wraps the official ``anthropic`` SDK.

Reads ``ANTHROPIC_API_KEY`` from the environment when ``api_key`` is not
supplied (the SDK does this natively).
"""
from __future__ import annotations

from typing import Any

from graphenda_build.llm.base import LLMError, LLMMessage, LLMProvider


class AnthropicLLMProvider(LLMProvider):
    """Anthropic Messages API provider."""

    name = "anthropic"

    DEFAULT_MODEL = "claude-opus-4-7"

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
            from anthropic import Anthropic
        except ImportError as exc:
            raise LLMError(
                "anthropic SDK is not installed. Add 'anthropic' to your deps."
            ) from exc

        kwargs: dict[str, Any] = {"timeout": timeout}
        if api_key:
            kwargs["api_key"] = api_key
        if base_url:
            kwargs["base_url"] = base_url
        self._client = Anthropic(**kwargs)

    def complete(
        self,
        messages: list[LLMMessage],
        system: str | None = None,
        model: str | None = None,
        max_tokens: int = 2048,
        temperature: float = 0.3,
        **kwargs: Any,
    ) -> str:
        api_messages = [{"role": m.role, "content": m.content} for m in messages]

        call_kwargs: dict[str, Any] = {
            "model": model or self.model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": api_messages,
        }
        if system:
            call_kwargs["system"] = system
        for k in ("top_p", "top_k", "stop_sequences"):
            if k in kwargs:
                call_kwargs[k] = kwargs[k]

        try:
            response = self._client.messages.create(**call_kwargs)
        except Exception as exc:
            raise LLMError(f"Anthropic call failed: {exc}") from exc

        parts: list[str] = []
        for block in response.content:
            text = getattr(block, "text", None)
            if isinstance(text, str):
                parts.append(text)
        return "".join(parts)
