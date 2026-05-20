"""Synchronous LLM provider contract used across graphenda-build.

The library only needs a single primitive: send a system prompt + a
conversation and get back the assistant text. No streaming, no tool calling,
no vision — the pipeline is batch and synchronous. Adapters in sibling
modules translate this contract into vendor-native calls.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Literal

Role = Literal["system", "user", "assistant"]


@dataclass
class LLMMessage:
    """One turn of the conversation in canonical form.

    The system prompt is passed separately to :meth:`LLMProvider.complete`,
    not as a message — keeps adapters simple and matches how every vendor
    expects it.
    """

    role: Role
    content: str


class LLMError(RuntimeError):
    """Raised on unrecoverable provider failures (auth, repeated 5xx, etc)."""


class LLMProvider(ABC):
    """Synchronous text-in / text-out LLM provider.

    Subclasses translate canonical inputs into the vendor format and return
    the assistant text. Errors that cannot be recovered must raise
    :class:`LLMError`.
    """

    name: str

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
        timeout: float = 120.0,
        **extra: Any,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.timeout = timeout
        self.extra = extra

    @abstractmethod
    def complete(
        self,
        messages: list[LLMMessage],
        system: str | None = None,
        model: str | None = None,
        max_tokens: int = 2048,
        temperature: float = 0.3,
        **kwargs: Any,
    ) -> str:
        """Send one turn and return the assistant text.

        Args:
            messages: Canonical conversation (system prompt excluded).
            system: System prompt string. ``None`` means no system prompt.
            model: Model id override. Falls back to ``self.model`` when ``None``.
            max_tokens: Cap on output tokens.
            temperature: Sampling temperature.
            **kwargs: Vendor-specific extras (``top_p``, ...). Adapters
                silently ignore unknown keys.

        Returns:
            The assistant text.

        Raises:
            LLMError: On unrecoverable failures.
        """

    def __repr__(self) -> str:
        return f"<{type(self).__name__} name={self.name!r} model={self.model!r}>"
