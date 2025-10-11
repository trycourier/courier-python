# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.paging import Paging

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
