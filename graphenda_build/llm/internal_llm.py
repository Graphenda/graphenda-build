"""Internal corporate ``/chatCompletion`` endpoint (text-only, sync).

Wire payload:

    POST <base_url>
    Headers: {user-uuid: <uuid>, Content-Type: application/json}
    Body:
        {"data": {
            "solicitacao": {"messages": [{"role": ..., "content": ...}, ...]},
            "config": {"temperature": float, "max_tokens": int, "top_p": float}
        }}

Response:

    {"data": "<assistant text>"}

A response of ``{"data": null}`` with HTTP 200 means the upstream LLM
transiently failed — the provider retries with exponential backoff.

The endpoint does not echo a model id and ignores any model passed by the
client; the deployment is pinned server-side.
"""
from __future__ import annotations

import logging
import time
from typing import Any

import httpx

from graphenda_build.llm.base import LLMError, LLMMessage, LLMProvider

logger = logging.getLogger(__name__)


class InternalLLMProvider(LLMProvider):
    """Internal /chatCompletion endpoint — single-shot text completion."""

    name = "internal-llm"

    DEFAULT_TIMEOUT = 120.0

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        user_uuid: str | None = None,
        max_retries: int = 3,
        retry_delay: float = 5.0,
        **extra: Any,
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            model=model,
            timeout=timeout,
            **extra,
        )
        self.endpoint = base_url
        self.user_uuid = user_uuid
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self._client = httpx.Client(timeout=timeout)

    def close(self) -> None:
        self._client.close()

    def __del__(self) -> None:
        try:
            self._client.close()
        except Exception:
            pass

    def _flatten(
        self, messages: list[LLMMessage], system: str | None
    ) -> list[dict[str, str]]:
        out: list[dict[str, str]] = []
        if system:
            out.append({"role": "system", "content": system})
        for m in messages:
            out.append({"role": m.role, "content": m.content})
        return out

    def complete(
        self,
        messages: list[LLMMessage],
        system: str | None = None,
        model: str | None = None,
        max_tokens: int = 2048,
        temperature: float = 0.3,
        **kwargs: Any,
    ) -> str:
        if not self.endpoint:
            raise LLMError(
                "internal-llm requires base_url (the endpoint URL). "
                "Set INTERNAL_LLM_ENDPOINT or pass base_url to build_provider."
            )
        if not self.user_uuid:
            raise LLMError(
                "internal-llm requires user_uuid. Set INTERNAL_LLM_USER_UUID "
                "or pass user_uuid to build_provider."
            )

        api_messages = self._flatten(messages, system)
        top_p = kwargs.get("top_p", 0.95)

        payload: dict[str, Any] = {
            "data": {
                "solicitacao": {"messages": api_messages},
                "config": {
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "top_p": top_p,
                },
            },
        }
        headers = {
            "user-uuid": self.user_uuid,
            "Content-Type": "application/json",
            "accept": "application/json",
        }

        last_error: str | None = None
        for attempt in range(self.max_retries):
            try:
                resp = self._client.post(
                    self.endpoint, headers=headers, json=payload
                )
            except httpx.HTTPError as exc:
                last_error = f"network error: {exc}"
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))
                    continue
                raise LLMError(last_error) from exc

            if resp.status_code >= 400:
                last_error = f"HTTP {resp.status_code}: {resp.text[:200]}"
                if attempt < self.max_retries - 1 and resp.status_code >= 500:
                    time.sleep(self.retry_delay * (attempt + 1))
                    continue
                raise LLMError(last_error)

            try:
                body = resp.json()
            except ValueError as exc:
                raise LLMError(
                    f"endpoint returned non-JSON response: {exc}"
                ) from exc

            data = body.get("data") if isinstance(body, dict) else None
            if data is None:
                last_error = (
                    f"endpoint returned data=null "
                    f"(attempt {attempt + 1}/{self.max_retries})"
                )
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))
                    continue
                raise LLMError(last_error)

            return data if isinstance(data, str) else str(data)

        raise LLMError(last_error or "internal-llm failed after retries")
