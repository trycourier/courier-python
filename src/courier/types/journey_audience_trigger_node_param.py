# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .journey_conditions_field_param import JourneyConditionsFieldParam

__all__ = ["JourneyAudienceTriggerNodeParam"]


class JourneyAudienceTriggerNodeParam(TypedDict, total=False):
    """Trigger fired when a user newly matches an Audience.

    Leaving and re-joining the Audience re-enters the Journey. Membership is new-members-only: users already in the Audience when the Journey is published do not enter. Unlike the v2 Automations audience trigger, there is no member scope, event type, or frequency mode to configure, and `audience_id` must name one Audience — wildcards are not supported.
    """

    audience_id: Required[str]
    """The Audience to watch.

    Must name a single Audience; wildcards are not supported.
    """

    trigger_type: Required[Literal["audience"]]

    type: Required[Literal["trigger"]]

    id: str

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """
