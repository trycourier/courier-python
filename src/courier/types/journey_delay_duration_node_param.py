# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .journey_conditions_field_param import JourneyConditionsFieldParam

__all__ = ["JourneyDelayDurationNodeParam"]


class JourneyDelayDurationNodeParam(TypedDict, total=False):
    """Pause the journey run for a fixed `duration`."""

    duration: Required[str]

    mode: Required[Literal["duration"]]

    type: Required[Literal["delay"]]

    id: str

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """
