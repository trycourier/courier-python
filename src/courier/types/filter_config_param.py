# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .single_filter_config_param import SingleFilterConfigParam

__all__ = ["FilterConfigParam"]

if TYPE_CHECKING or not PYDANTIC_V1:
    FilterConfigParam = TypeAliasType("FilterConfigParam", Union[SingleFilterConfigParam, "NestedFilterConfigParam"])
else:
    FilterConfigParam: TypeAlias = Union[SingleFilterConfigParam, "NestedFilterConfigParam"]

from .nested_filter_config_param import NestedFilterConfigParam
