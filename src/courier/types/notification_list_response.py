# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.paging import Paging
from .notification_template_summary import NotificationTemplateSummary

__all__ = [
    "NotificationListResponse",
    "Result",
    "ResultNotification",
    "ResultNotificationTags",
    "ResultNotificationTagsData",
]


class ResultNotificationTagsData(BaseModel):
    id: str

    name: str


class ResultNotificationTags(BaseModel):
    data: List[ResultNotificationTagsData]


class ResultNotification(BaseModel):
    id: str

    created_at: int

    event_ids: List[str]
    """Array of event IDs associated with this notification"""

    routing: "MessageRouting"

    topic_id: str

    updated_at: int

    note: Optional[str] = None

    tags: Optional[ResultNotificationTags] = None

    title: Optional[str] = None


Result: TypeAlias = Union[ResultNotification, NotificationTemplateSummary]


class NotificationListResponse(BaseModel):
    paging: Paging

    results: List[Result]
    """Notification templates in this workspace."""


from .shared.message_routing import MessageRouting
