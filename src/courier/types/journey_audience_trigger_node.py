# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .journey_conditions_field import JourneyConditionsField

__all__ = ["JourneyAudienceTriggerNode"]


class JourneyAudienceTriggerNode(BaseModel):
    """Trigger fired when a user newly matches an Audience.

    Leaving and re-joining the Audience re-enters the Journey. Membership is new-members-only: users already in the Audience when the Journey is published do not enter. Unlike the v2 Automations audience trigger, there is no member scope, event type, or frequency mode to configure, and `audience_id` must name one Audience — wildcards are not supported.
    """

    audience_id: str
    """The Audience to watch.

    Must name a single Audience; wildcards are not supported.
    """

    trigger_type: Literal["audience"]

    type: Literal["trigger"]

    id: Optional[str] = None

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """
