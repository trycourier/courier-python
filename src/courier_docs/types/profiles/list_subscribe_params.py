# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..lists.recipient_preferences_param import RecipientPreferencesParam

__all__ = ["ListSubscribeParams", "List"]


class ListSubscribeParams(TypedDict, total=False):
    lists: Required[Iterable[List]]


class List(TypedDict, total=False):
    list_id: Required[Annotated[str, PropertyInfo(alias="listId")]]

    preferences: Optional[RecipientPreferencesParam]
