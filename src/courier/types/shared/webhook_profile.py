# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .webhook_method import WebhookMethod
from .webhook_profile_type import WebhookProfileType
from .webhook_authentication import WebhookAuthentication

__all__ = ["WebhookProfile"]


class WebhookProfile(BaseModel):
    url: str
    """The URL to send the webhook request to."""

    authentication: Optional[WebhookAuthentication] = None
    """Authentication configuration for the webhook request."""

    headers: Optional[Dict[str, str]] = None
    """Custom headers to include in the webhook request."""

    method: Optional[WebhookMethod] = None
    """The HTTP method to use for the webhook request.

    Defaults to POST if not specified.
    """

    profile: Optional[WebhookProfileType] = None
    """Specifies what profile information is included in the request payload.

    Defaults to 'limited' if not specified.
    """
