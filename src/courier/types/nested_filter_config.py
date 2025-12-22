# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NestedFilterConfig"]


class NestedFilterConfig(BaseModel):
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

    rules: List["FilterConfig"]


from .filter_config import FilterConfig
