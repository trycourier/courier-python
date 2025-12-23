# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ListFilter"]


class ListFilter(TypedDict, total=False):
    operator: Required[Literal["MEMBER_OF"]]
    """Send to users only if they are member of the account"""

    path: Required[Literal["account_id"]]

    value: Required[str]
