# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..shared.webhook_auth_mode import WebhookAuthMode

__all__ = ["WebhookAuthentication"]


class WebhookAuthentication(TypedDict, total=False):
    mode: Required[WebhookAuthMode]
    """The authentication mode to use. Defaults to 'none' if not specified."""

    token: Optional[str]
    """Token for bearer authentication."""

    password: Optional[str]
    """Password for basic authentication."""

    username: Optional[str]
    """Username for basic authentication."""
