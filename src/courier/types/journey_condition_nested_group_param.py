# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .journey_condition_group_param import JourneyConditionGroupParam

__all__ = ["JourneyConditionNestedGroupParam"]


class JourneyConditionNestedGroupParam(TypedDict, total=False):
    """A nested condition group.

    Exactly one of `AND` or `OR` must be present at runtime; each is a list of `JourneyConditionGroup` items.
    """

    and_: Annotated[Iterable[JourneyConditionGroupParam], PropertyInfo(alias="AND")]

    or_: Annotated[Iterable[JourneyConditionGroupParam], PropertyInfo(alias="OR")]
