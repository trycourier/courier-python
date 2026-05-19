# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .journey_conditions_field_param import JourneyConditionsFieldParam

__all__ = ["JourneyThrottleDynamicNodeParam"]


class JourneyThrottleDynamicNodeParam(TypedDict, total=False):
    """
    Throttle the journey by a dynamic `throttle_key`, allowing at most `max_allowed` invocations per `period`.
    """

    max_allowed: Required[int]

    period: Required[str]

    scope: Required[Literal["dynamic"]]

    throttle_key: Required[str]

    type: Required[Literal["throttle"]]

    id: str

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """
