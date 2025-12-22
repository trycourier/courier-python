# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .webhook_profile import WebhookProfile

__all__ = ["WebhookRecipient"]


class WebhookRecipient(TypedDict, total=False):
    """Send via webhook"""

    webhook: Required[WebhookProfile]
