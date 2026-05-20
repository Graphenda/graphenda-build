"""Internal ``/chatCompletion`` provider with context-window management.

Same transport as :class:`InternalLLMProvider` but adds two safeguards for
the 60s server-side timeout and 128k input-token limit:

- **Timeout-aware retry.** Default client timeout is 55s; a httpx timeout
  retries once with halved ``max_tokens``.
- **Input-token trimming.** Before each POST the provider estimates input
  tokens (char/4 heuristic) and, if over ``max_input_tokens``, drops the
  oldest middle messages while preserving the system prompt, the first
  user message and the most recent turns.

The text tool-calling protocol from vulpcode is intentionally **not** ported
— graphenda-build never asks the LLM to call tools (the ontology is injected
as a prompt constraint, not as a tool schema).
"""
from __future__ import annotations

import logging
import time
from typing import Any

import httpx

from graphenda_build.llm.base import LLMError, LLMMessage, LLMProvider

logger = logging.getLogger(__name__)


class InternalLLMAgenticProvider(LLMProvider):
    """Internal /chatCompletion with budget-aware retries and trimming."""

    name = "internal-llm-agentic"

    DEFAULT_TIMEOUT = 55.0
    DEFAULT_MAX_INPUT_TOKENS = 115_000
    _CHARS_PER_TOKEN = 4
    _PRESERVE_TAIL = 2
    _MIN_MAX_TOKENS = 500

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        user_uuid: str | None = None,
        max_retries: int = 3,
        retry_delay: float = 5.0,
        max_input_tokens: int = DEFAULT_MAX_INPUT_TOKENS,
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
        self.max_input_tokens = max_input_tokens
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

    @classmethod
    def _estimate_tokens(cls, text: str) -> int:
        if not text:
            return 0
        return max(1, len(text) // cls._CHARS_PER_TOKEN)

    @classmethod
    def _messages_tokens(cls, msgs: list[dict[str, str]]) -> int:
        return sum(cls._estimate_tokens(m.get("content", "")) for m in msgs)

    def _fit_budget(
        self, api_messages: list[dict[str, str]]
    ) -> tuple[list[dict[str, str]], int]:
        """Drop oldest middle messages so estimated tokens fit the budget.

        Preserves the system prompt, the first user message, and the last
        ``_PRESERVE_TAIL`` messages. Returns ``(msgs, dropped_count)``.
        """
        limit = self.max_input_tokens
        total = self._messages_tokens(api_messages)
        if total <= limit:
            return api_messages, 0

        msgs = list(api_messages)
        n = len(msgs)
        head = min(2, n)
        tail_start = max(head, n - self._PRESERVE_TAIL)

        middle = list(range(head, tail_start))
        dropped = 0
        while total > limit and middle:
            drop_idx = middle.pop(0)
            total -= self._estimate_tokens(msgs[drop_idx].get("content", ""))
            dropped += 1

        if dropped == 0:
            return msgs, 0

        rebuilt = (
            msgs[:head]
            + [msgs[i] for i in middle]
            + msgs[tail_start:]
        )
        placeholder = {
            "role": "user",
            "content": (
                f"[{dropped} earlier message(s) omitted to fit the "
                f"{limit}-token context window]"
            ),
        }
        rebuilt.insert(head, placeholder)
        return rebuilt, dropped

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
                "internal-llm-agentic requires base_url. Set "
                "INTERNAL_LLM_ENDPOINT or pass base_url to build_provider."
            )
        if not self.user_uuid:
            raise LLMError(
                "internal-llm-agentic requires user_uuid. Set "
                "INTERNAL_LLM_USER_UUID or pass user_uuid to build_provider."
            )

        api_messages = self._flatten(messages, system)
        api_messages, dropped = self._fit_budget(api_messages)
        if dropped:
            logger.info(
                "Trimmed %d old message(s) to fit %d-token budget",
                dropped, self.max_input_tokens,
            )

        top_p = kwargs.get("top_p", 0.95)
        current_max_tokens = max_tokens

        payload: dict[str, Any] = {
            "data": {
                "solicitacao": {"messages": api_messages},
                "config": {
                    "temperature": temperature,
                    "max_tokens": current_max_tokens,
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
            except httpx.TimeoutException as exc:
                last_error = f"timeout after {self.timeout}s: {exc}"
                if attempt < self.max_retries - 1:
                    current_max_tokens = max(
                        self._MIN_MAX_TOKENS, current_max_tokens // 2
                    )
                    payload["data"]["config"]["max_tokens"] = current_max_tokens
                    logger.info(
                        "Timeout — retrying with max_tokens=%d",
                        current_max_tokens,
                    )
                    time.sleep(self.retry_delay * (attempt + 1))
                    continue
                raise LLMError(
                    f"endpoint exceeded {self.timeout}s timeout after "
                    f"{self.max_retries} attempts."
                ) from exc
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
                    f"endpoint returned non-JSON: {exc}"
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

        raise LLMError(last_error or "internal-llm-agentic failed after retries")
