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
    validation error.
    """

    title: str
    """Optional display title. Omit to use "Default Configuration"."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]
