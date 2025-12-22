# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .webhook_auth_mode import WebhookAuthMode

__all__ = ["WebhookAuthentication"]


class WebhookAuthentication(BaseModel):
    mode: WebhookAuthMode
    """The authentication mode to use. Defaults to 'none' if not specified."""

    token: Optional[str] = None
    """Token for bearer authentication."""

    password: Optional[str] = None
    """Password for basic authentication."""

    username: Optional[str] = None
    """Username for basic authentication."""
