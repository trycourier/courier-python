# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProviderCreateParams"]


class ProviderCreateParams(TypedDict, total=False):
    provider: Required[str]
    """The provider key identifying the type (e.g.

    "sendgrid", "twilio"). Must be a known Courier provider — see the catalog
    endpoint for valid keys.
    """

    alias: str
    """Optional alias for this configuration."""

    settings: Dict[str, object]
    """Provider-specific settings (snake_case keys).

    Defaults to an empty object when omitted. Use the catalog endpoint to discover
    required fields for a given provider — omitting a required field returns a 400
    validation error. Set `rate_limit` to cap this configuration's send rate:
    `{ "rate": <number greater than 0>, "period": "second" | "minute" | "hour" }`,
    e.g. `{ "rate": 0.5, "period": "minute" }` for one send every 2 minutes. The
    interval between sends (`period` divided by `rate`) must be from 1 millisecond
    to 12 hours, otherwise the request returns a 400 `InvalidRateLimit` error. The
    limit applies per configuration and per environment (a test-environment
    configuration has its own limit). Sends above the rate are queued, not dropped,
    and changes take up to 60 seconds to apply. It has no effect on observability or
    CDP integrations, which do not send messages. Omit it or set it to null for no
    limit.
    """

    title: str
    """Optional display title. Omit to use "Default Configuration"."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]
