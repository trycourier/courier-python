# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .shared.user_recipient import UserRecipient
from .shared.recipient_preferences import RecipientPreferences

__all__ = ["InboundBulkMessageUser"]


class InboundBulkMessageUser(BaseModel):
    data: Optional[object] = None
    """User-specific data that will be merged with message.data"""

    preferences: Optional[RecipientPreferences] = None

    profile: Optional[Dict[str, object]] = None
    """User profile information.

    For email-based bulk jobs, `profile.email` is required for provider routing to
    determine if the message can be delivered. The email address should be provided
    here rather than in `to.email`.
    """

    recipient: Optional[str] = None
    """User ID (legacy field, use profile or to.user_id instead)"""

    to: Optional[UserRecipient] = None
    """Optional recipient information.

    Note: For email provider routing, use `profile.email` instead of `to.email`. The
    `to` field is primarily used for recipient identification and data merging.
    """
