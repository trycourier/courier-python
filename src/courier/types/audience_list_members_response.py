# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .paging import Paging
from .._models import BaseModel

__all__ = ["AudienceListMembersResponse", "Item"]


class Item(BaseModel):
    added_at: str

    audience_id: str

    audience_version: int

    member_id: str

    reason: str


class AudienceListMembersResponse(BaseModel):
    items: List[Item]

    paging: Paging
