# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .journey_conditions_field import JourneyConditionsField

__all__ = ["JourneySegmentTriggerNode"]


class JourneySegmentTriggerNode(BaseModel):
    """Trigger fired by a segment event (`identify`, `group`, `track`, or `page`).

    A trigger with no `event_id` fires on any event of its type — the only shape `identify` and `group` can take, and the one that catches a stock `analytics.page()` call.
    """

    request_type: Literal["identify", "group", "track", "page"]

    trigger_type: Literal["segment"]

    type: Literal["trigger"]

    id: Optional[str] = None

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    event_id: Optional[str] = None
