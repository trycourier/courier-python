# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["Filter", "UnionMember0"]


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


Filter: TypeAlias = Union[UnionMember0, "NestedFilterConfig"]

from .nested_filter_config import NestedFilterConfig
