# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .user_recipient import UserRecipient
from .recipient_preferences import RecipientPreferences

__all__ = ["InboundBulkMessageUser"]


class InboundBulkMessageUser(TypedDict, total=False):
    data: object

    preferences: Optional[RecipientPreferences]

    profile: object

    recipient: Optional[str]

    to: Optional[UserRecipient]
