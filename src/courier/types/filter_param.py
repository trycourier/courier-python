# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["FilterParam", "UnionMember0"]


class UnionMember0(TypedDict, total=False):
    operator: Required[
        Literal[
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
    ]
    """The operator to use for filtering"""

    path: Required[str]
    """
    The attribe name from profile whose value will be operated against the filter
    value
    """

    value: Required[str]
    """The value to use for filtering"""


FilterParam: TypeAlias = Union[UnionMember0, "NestedFilterConfigParam"]

from .nested_filter_config_param import NestedFilterConfigParam
