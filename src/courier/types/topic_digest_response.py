# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .topic_digest_category import TopicDigestCategory
from .topic_digest_schedule_response import TopicDigestScheduleResponse

__all__ = ["TopicDigestResponse"]


class TopicDigestResponse(BaseModel):
    """A topic's digest configuration."""

    categories: List[TopicDigestCategory]
    """Retention rules per category key."""

    schedules: List[TopicDigestScheduleResponse]
    """The digest's delivery cadences, each with its server-assigned `schedule_id`."""

    template_id: str
    """The notification template that renders the digest."""

    audience_id: Optional[str] = None
    """The audience the digest is scoped to, when set."""

    created: Optional[str] = None
    """ISO-8601 timestamp of when the digest was configured."""

    trigger_empty: Optional[bool] = None
    """Whether the digest is delivered even when nothing was collected."""

    updated: Optional[str] = None
    """ISO-8601 timestamp of the last update."""
