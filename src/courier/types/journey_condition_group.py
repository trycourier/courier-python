# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .journey_condition_atom import JourneyConditionAtom

__all__ = ["JourneyConditionGroup"]


class JourneyConditionGroup(BaseModel):
    """A leaf condition group.

    Exactly one of `AND` or `OR` must be present at runtime; each is a list of `JourneyConditionAtom` tuples.
    """

    and_: Optional[List[JourneyConditionAtom]] = FieldInfo(alias="AND", default=None)

    or_: Optional[List[JourneyConditionAtom]] = FieldInfo(alias="OR", default=None)
