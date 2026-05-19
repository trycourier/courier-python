# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .journey_conditions_field import JourneyConditionsField

__all__ = ["JourneyThrottleDynamicNode"]


class JourneyThrottleDynamicNode(BaseModel):
    """
    Throttle the journey by a dynamic `throttle_key`, allowing at most `max_allowed` invocations per `period`.
    """

    max_allowed: int

    period: str

    scope: Literal["dynamic"]

    throttle_key: str

    type: Literal["throttle"]

    id: Optional[str] = None

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """
