# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .user_recipient_param import UserRecipientParam

__all__ = ["RecipientParam", "ListRecipient"]


class ListRecipient(TypedDict, total=False):
    data: Optional[Dict[str, object]]

    list_id: Optional[str]


RecipientParam: TypeAlias = Union[UserRecipientParam, ListRecipient]
