# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .single_filter_config import SingleFilterConfig

__all__ = ["FilterConfig"]

if TYPE_CHECKING or not PYDANTIC_V1:
    FilterConfig = TypeAliasType("FilterConfig", Union[SingleFilterConfig, "NestedFilterConfig"])
else:
    FilterConfig: TypeAlias = Union[SingleFilterConfig, "NestedFilterConfig"]

from .nested_filter_config import NestedFilterConfig
