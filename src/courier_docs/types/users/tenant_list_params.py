# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TenantListParams"]


class TenantListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Continue the pagination with the next cursor"""

    limit: Optional[int]
    """The number of accounts to return (defaults to 20, maximum value of 100)"""
