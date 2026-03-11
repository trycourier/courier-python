# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["JourneyListParams"]


class JourneyListParams(TypedDict, total=False):
    cursor: str
    """A cursor token for pagination.

    Use the cursor from the previous response to fetch the next page of results.
    """

    version: Literal["published", "draft"]
    """The version of journeys to retrieve.

    Accepted values are published (for published journeys) or draft (for draft
    journeys). Defaults to published.
    """
