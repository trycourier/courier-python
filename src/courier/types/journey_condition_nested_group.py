# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .journey_condition_group import JourneyConditionGroup

__all__ = ["JourneyConditionNestedGroup"]


class JourneyConditionNestedGroup(BaseModel):
    """A nested condition group.

    Exactly one of `AND` or `OR` must be present at runtime; each is a list of `JourneyConditionGroup` items.
    """

    and_: Optional[List[JourneyConditionGroup]] = FieldInfo(alias="AND", default=None)

    or_: Optional[List[JourneyConditionGroup]] = FieldInfo(alias="OR", default=None)
