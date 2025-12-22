# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..shared.webhook_method import WebhookMethod
from .webhook_authentication import WebhookAuthentication
from ..shared.webhook_profile_type import WebhookProfileType

__all__ = ["WebhookProfile"]


class WebhookProfile(TypedDict, total=False):
    url: Required[str]
    """The URL to send the webhook request to."""

    authentication: Optional[WebhookAuthentication]
    """Authentication configuration for the webhook request."""

    headers: Optional[Dict[str, str]]
    """Custom headers to include in the webhook request."""

    method: Optional[WebhookMethod]
    """The HTTP method to use for the webhook request.

    Defaults to POST if not specified.
    """

    profile: Optional[WebhookProfileType]
    """Specifies what profile information is included in the request payload.

    Defaults to 'limited' if not specified.
    """
