# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Provider"]


class Provider(BaseModel):
    """A configured provider in the workspace."""

    id: str
    """A unique identifier for the provider configuration."""

    created: int
    """Unix timestamp (ms) of when the provider was created."""

    provider: str
    """The provider key (e.g. "sendgrid", "twilio", "slack")."""

    settings: Dict[str, object]
    """Provider-specific settings (snake_case keys on the wire)."""

    title: str
    """Display title. Defaults to "Default Configuration" when not explicitly set."""

    alias: Optional[str] = None
    """Optional alias for this configuration."""

    updated: Optional[int] = None
    """Unix timestamp (ms) of when the provider was last updated."""
