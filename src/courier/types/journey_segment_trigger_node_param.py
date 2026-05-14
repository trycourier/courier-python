# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .journey_conditions_field_param import JourneyConditionsFieldParam

__all__ = ["JourneySegmentTriggerNodeParam"]


class JourneySegmentTriggerNodeParam(TypedDict, total=False):
    request_type: Required[Literal["identify", "group", "track"]]

    trigger_type: Required[Literal["segment"]]

    type: Required[Literal["trigger"]]

    id: str

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    event_id: str
