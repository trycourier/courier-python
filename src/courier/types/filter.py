# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Filter"]


class Filter(BaseModel):
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
