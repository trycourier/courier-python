# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .shared_params.user_recipient import UserRecipient
from .shared_params.recipient_preferences import RecipientPreferences

__all__ = ["InboundBulkMessageUserParam"]


class InboundBulkMessageUserParam(TypedDict, total=False):
    data: object
    """User-specific data that will be merged with message.data"""

    preferences: Optional[RecipientPreferences]

    profile: Optional[Dict[str, object]]
    """User profile information.

    For email-based bulk jobs, `profile.email` is required for provider routing to
    determine if the message can be delivered. The email address should be provided
    here rather than in `to.email`.
    """

    recipient: Optional[str]
    """User ID (legacy field, use profile or to.user_id instead)"""

    to: Optional[UserRecipient]
    """Optional recipient information.

    Note: For email provider routing, use `profile.email` instead of `to.email`. The
    `to` field is primarily used for recipient identification and data merging.
    """
