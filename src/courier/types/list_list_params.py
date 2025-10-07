# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ListListParams"]


class ListListParams(TypedDict, total=False):
    cursor: Optional[str]
    """A unique identifier that allows for fetching the next page of lists."""

    pattern: Optional[str]
    """\"A pattern used to filter the list items returned.

    Pattern types supported: exact match on `list_id` or a pattern of one or more
    pattern parts. you may replace a part with either: `*` to match all parts in
    that position, or `**` to signify a wildcard `endsWith` pattern match."
    """
