"""Google Gemini adapter — wraps the ``google-genai`` SDK.

Gemini's API takes the system instruction at client/model configuration
time rather than in the message list; this adapter handles that wiring so
callers can keep using the same ``complete(system=...)`` signature.
"""
from __future__ import annotations

from typing import Any

from graphenda_build.llm.base import LLMError, LLMMessage, LLMProvider


class GeminiLLMProvider(LLMProvider):
    """Google Gemini provider."""

    name = "gemini"

    DEFAULT_MODEL = "gemini-2.0-flash"

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
            from google import genai
        except ImportError as exc:
            raise LLMError(
                "google-genai SDK is not installed. "
                "Install with: pip install google-genai"
            ) from exc

        self._genai = genai
        self._client = genai.Client(api_key=api_key) if api_key else genai.Client()

    def complete(
        self,
        messages: list[LLMMessage],
        system: str | None = None,
        model: str | None = None,
        max_tokens: int = 2048,
        temperature: float = 0.3,
        **kwargs: Any,
    ) -> str:
        contents: list[dict[str, Any]] = []
        for m in messages:
            role = "user" if m.role == "user" else "model"
            contents.append({"role": role, "parts": [{"text": m.content}]})

        from google.genai import types as gtypes

        cfg_kwargs: dict[str, Any] = {
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }
        if system:
            cfg_kwargs["system_instruction"] = system
        for k in ("top_p", "top_k"):
            if k in kwargs:
                cfg_kwargs[k] = kwargs[k]

        try:
            response = self._client.models.generate_content(
                model=model or self.model,
                contents=contents,
                config=gtypes.GenerateContentConfig(**cfg_kwargs),
            )
        except Exception as exc:
            raise LLMError(f"Gemini call failed: {exc}") from exc

        text = getattr(response, "text", None)
        if isinstance(text, str):
            return text
        return ""
