# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .user_recipient_param import UserRecipientParam
from .lists.recipient_preferences_param import RecipientPreferencesParam

__all__ = ["InboundBulkMessageUserParam"]


class InboundBulkMessageUserParam(TypedDict, total=False):
    data: object

    preferences: Optional[RecipientPreferencesParam]

    profile: object

    recipient: Optional[str]

    to: Optional[UserRecipientParam]
