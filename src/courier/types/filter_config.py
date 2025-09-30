# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["FilterConfig", "UnionMember0"]


class UnionMember0(BaseModel):
    operator: Literal[
        "ENDS_WITH",
        "EQ",
        "EXISTS",
        "GT",
        "GTE",
        "INCLUDES",
        "IS_AFTER",
        "IS_BEFORE",
        "LT",
        "LTE",
        "NEQ",
        "OMIT",
        "STARTS_WITH",
        "AND",
        "OR",
    ]
    """The operator to use for filtering"""

    path: str
    """
    The attribe name from profile whose value will be operated against the filter
    value
    """

    value: str
    """The value to use for filtering"""


if TYPE_CHECKING or not PYDANTIC_V1:
    FilterConfig = TypeAliasType("FilterConfig", Union[UnionMember0, "NestedFilterConfig"])
else:
    FilterConfig: TypeAlias = Union[UnionMember0, "NestedFilterConfig"]

from .nested_filter_config import NestedFilterConfig
