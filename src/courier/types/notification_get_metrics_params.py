# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NotificationGetMetricsParams"]


class NotificationGetMetricsParams(TypedDict, total=False):
    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end of the window, as an ISO 8601 timestamp with an offset.

    Must be supplied together with `start`. An `end` in the future is accepted and
    not clamped — the trailing buckets come back empty.
    """

    granularity: Literal["HOUR", "DAY", "WEEK", "MONTH"]
    """The size of each bucket in the series.

    Defaults to `DAY`. `WEEK` buckets start on Sunday. A fine granularity caps the
    window it can cover: `HOUR` spans at most 7 days and `DAY` at most 90 days, and
    a wider window returns `400` — request a coarser granularity instead. `WEEK` and
    `MONTH` are uncapped, subject to the 1000-bucket limit on a single response.
    """

    lookback: str
    """
    The length of the window, counted back from now, as an ISO 8601 duration
    (`P30D`, `P12W`, `PT12H`). Defaults to `P30D`, and is ignored when `start` and
    `end` are supplied. A malformed or non-positive duration returns `400`.
    """

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The inclusive start of the window, as an ISO 8601 timestamp with an offset
    (`2026-04-01T00:00:00Z`). Must be supplied together with `end` and be earlier
    than it; either one alone returns `400`.
    """
