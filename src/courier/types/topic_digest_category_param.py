# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TopicDigestCategoryParam"]


class TopicDigestCategoryParam(TypedDict, total=False):
    """
    How events collected under a category key are retained when a digest holds more than it will render.
    """

    category_key: Required[str]
    """The key that identifies the category within the digest."""

    limit: int
    """How many collected events are carried into the rendered digest. Defaults to 10.

    Events beyond the limit are discarded, not held back for the next digest: the
    release consumes everything collected so far and only `limit` of them appear.
    `retain` decides which ones those are.
    """

    retain: Literal["FIRST", "LAST", "HIGHEST", "LOWEST", "NONE"]
    """Which collected events survive the `limit`.

    `FIRST` and `LOWEST` keep the earliest or smallest; `LAST` and `HIGHEST` keep
    the latest or largest. Accepted case-insensitively, returned uppercase.
    """

    sort_key: str
    """The data key used to rank events.

    Required when `retain` is `HIGHEST` or `LOWEST`.
    """
