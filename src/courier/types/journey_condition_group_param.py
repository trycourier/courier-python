# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .journey_condition_atom_param import JourneyConditionAtomParam

__all__ = ["JourneyConditionGroupParam"]


class JourneyConditionGroupParam(TypedDict, total=False):
    """A leaf condition group.

    Exactly one of `AND` or `OR` must be present at runtime; each is a list of `JourneyConditionAtom` tuples.
    """

    and_: Annotated[Iterable[JourneyConditionAtomParam], PropertyInfo(alias="AND")]

    or_: Annotated[Iterable[JourneyConditionAtomParam], PropertyInfo(alias="OR")]
