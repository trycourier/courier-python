# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NotificationMetricsResponse", "Series", "SeriesData"]


class SeriesData(BaseModel):
    channel: str
    """Channel the provider delivered on, e.g. `email`."""

    clicked: int
    """Messages with at least one tracked link click."""

    delivered: int
    """Messages the provider confirmed as delivered."""

    errors: int
    """
    Messages the provider rejected or failed on, including ones a later provider
    then delivered.
    """

    opened: int
    """Messages opened at least once. Always `0` on channels with no open tracking."""

    provider: str
    """Provider that handled the messages, e.g. `sendgrid`."""

    sent: int
    """Messages handed to the provider."""

    undeliverable: int
    """Messages Courier could not deliver on any provider for the channel."""


class Series(BaseModel):
    data: List[SeriesData]
    """One entry per provider and channel that handled a message in this bucket.

    Empty when nothing was sent.
    """

    period: datetime
    """Start of the bucket, second-precision UTC."""


class NotificationMetricsResponse(BaseModel):
    end: datetime
    """End of the window actually queried, ceiled onto the granularity grid.

    Second-precision UTC.
    """

    granularity: Literal["HOUR", "DAY", "WEEK", "MONTH"]
    """Bucket size the series was built at."""

    notification_id: str = FieldInfo(alias="notificationId")
    """The template the series describes, echoed from the request."""

    series: List[Series]
    """
    One entry per bucket between `start` and `end`, oldest first, including buckets
    with no activity.
    """

    start: datetime
    """
    Inclusive start of the window actually queried, floored onto the granularity
    grid. Second-precision UTC.
    """
