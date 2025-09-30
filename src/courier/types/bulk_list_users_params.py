# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BulkListUsersParams"]


class BulkListUsersParams(TypedDict, total=False):
    cursor: Optional[str]
    """
    A unique identifier that allows for fetching the next set of users added to the
    bulk job
    """
