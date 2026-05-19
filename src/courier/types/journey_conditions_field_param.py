# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .journey_condition_atom_param import JourneyConditionAtomParam
from .journey_condition_group_param import JourneyConditionGroupParam
from .journey_condition_nested_group_param import JourneyConditionNestedGroupParam

__all__ = ["JourneyConditionsFieldParam"]

JourneyConditionsFieldParam: TypeAlias = Union[
    JourneyConditionAtomParam, JourneyConditionGroupParam, JourneyConditionNestedGroupParam
]
