# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .webhook_profile import WebhookProfile

__all__ = ["WebhookRecipient"]


class WebhookRecipient(BaseModel):
    """Send via webhook"""

    webhook: WebhookProfile
