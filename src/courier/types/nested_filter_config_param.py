# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NestedFilterConfigParam"]


class NestedFilterConfigParam(TypedDict, total=False):
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

    rules: Required[Iterable["FilterConfigParam"]]


from .filter_config_param import FilterConfigParam
