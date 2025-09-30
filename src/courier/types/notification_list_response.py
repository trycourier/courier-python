# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .paging import Paging
from .._models import BaseModel

__all__ = ["NotificationListResponse", "Result", "ResultTags", "ResultTagsData"]


class ResultTagsData(BaseModel):
    id: str

    name: str


class ResultTags(BaseModel):
    data: List[ResultTagsData]


class Result(BaseModel):
    id: str

    created_at: int

    note: str

    routing: "MessageRouting"

    topic_id: str

    updated_at: int

    tags: Optional[ResultTags] = None

    title: Optional[str] = None


class NotificationListResponse(BaseModel):
    paging: Paging

    results: List[Result]


from .message_routing import MessageRouting
