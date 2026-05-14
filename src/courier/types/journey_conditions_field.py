# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .journey_condition_atom import JourneyConditionAtom
from .journey_condition_group import JourneyConditionGroup
from .journey_condition_nested_group import JourneyConditionNestedGroup

__all__ = ["JourneyConditionsField"]

JourneyConditionsField: TypeAlias = Union[JourneyConditionAtom, JourneyConditionGroup, JourneyConditionNestedGroup]
