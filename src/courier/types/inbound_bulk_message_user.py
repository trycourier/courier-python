# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.user_recipient import UserRecipient
from .shared.recipient_preferences import RecipientPreferences

__all__ = ["InboundBulkMessageUser"]


class InboundBulkMessageUser(BaseModel):
    data: Optional[object] = None

    preferences: Optional[RecipientPreferences] = None

    profile: Optional[object] = None

    recipient: Optional[str] = None

    to: Optional[UserRecipient] = None
