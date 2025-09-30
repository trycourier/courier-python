# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..paging import Paging
from ..._models import BaseModel
from .recipient_preferences import RecipientPreferences

__all__ = ["SubscriptionListResponse", "Item"]


class Item(BaseModel):
    recipient_id: str = FieldInfo(alias="recipientId")

    created: Optional[str] = None

    preferences: Optional[RecipientPreferences] = None


class SubscriptionListResponse(BaseModel):
    items: List[Item]

    paging: Paging
