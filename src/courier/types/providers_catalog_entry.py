# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ProvidersCatalogEntry", "Settings"]


class Settings(BaseModel):
    """Describes a single configuration field in the provider catalog."""

    required: bool
    """Whether this field is required when configuring the provider."""

    type: str
    """The field's data type (e.g. "string", "boolean", "enum")."""

    values: Optional[List[str]] = None
    """Allowed values when `type` is "enum"."""


class ProvidersCatalogEntry(BaseModel):
    """A provider type from the catalog.

    Contains the key, display name, description, and a `settings` object describing configuration schema fields.
    """

    channel: str
    """Courier taxonomy channel (e.g.

    email, push, sms, direct_message, inbox, webhook).
    """

    description: str
    """Short description of the provider."""

    name: str
    """Human-readable display name."""

    provider: str
    """The provider key (e.g. "sendgrid", "twilio")."""

    settings: Dict[str, Settings]
    """Map of setting field names (snake_case) to their schema descriptors.

    Each descriptor has `type` and `required`. Empty when the provider has no
    configurable schema.
    """
