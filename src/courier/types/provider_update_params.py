# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ProviderUpdateParams"]


class ProviderUpdateParams(TypedDict, total=False):
    provider: Required[str]
    """The provider key identifying the type.

    Required on every request because it selects the provider-specific settings
    schema for validation.
    """

    alias: str
    """Updated alias. Omit to clear."""

    settings: Dict[str, object]
    """Provider-specific settings (snake_case keys).

    Replaces the full settings object — omitted settings fields are removed. Use the
    catalog endpoint to check required fields. Set `rate_limit` to cap this
    configuration's send rate:
    `{ "rate": <number greater than 0>, "period": "second" | "minute" | "hour" }`,
    e.g. `{ "rate": 0.5, "period": "minute" }` for one send every 2 minutes. The
    interval between sends (`period` divided by `rate`) must be from 1 millisecond
    to 12 hours, otherwise the request returns a 400 `InvalidRateLimit` error. The
    limit applies per configuration and per environment (a test-environment
    configuration has its own limit). Sends above the rate are queued, not dropped,
    and changes take up to 60 seconds to apply. It has no effect on observability or
    CDP integrations, which do not send messages. Omitting `rate_limit` or setting
    it to null removes any existing limit, including one set in Studio.
    """

    title: str
    """Updated display title."""
