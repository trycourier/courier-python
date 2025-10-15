# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .recipient_preferences import RecipientPreferences

__all__ = ["SubscribeToListsRequestItem"]


class SubscribeToListsRequestItem(BaseModel):
    list_id: str = FieldInfo(alias="listId")

    preferences: Optional[RecipientPreferences] = None
