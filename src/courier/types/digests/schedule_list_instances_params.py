# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScheduleListInstancesParams"]


class ScheduleListInstancesParams(TypedDict, total=False):
    cursor: str
    """
    A cursor token from a previous response, used to fetch the next page of results.
    """

    limit: int
    """The maximum number of digest instances to return.

    Defaults to 20, with a maximum of 100.
    """
