# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .digest_frequency import DigestFrequency
from .digest_day_of_week import DigestDayOfWeek

__all__ = ["TopicDigestScheduleResponse"]


class TopicDigestScheduleResponse(BaseModel):
    """A delivery cadence for a topic's digest, with its assigned id."""

    schedule_id: str
    """The schedule's identifier, assigned by the server.

    This is the value the `/digests/schedules/{schedule_id}` endpoints are keyed by.

    Two formats are in circulation and only one is safe to drop into a URL.
    Schedules created through the API are `sch_01m26xfcn3endt3nxy4e2kx2rh` and need
    no encoding. Schedules created in the Preferences Editor before that format are
    `sch/{uuid}` and contain a literal `/`, so they must be URL-encoded as
    `sch%2F{uuid}` — unencoded, the path does not match the route and the response
    is a bare `404` that reads like a broken endpoint. Existing ids are never
    migrated.
    """

    created: Optional[str] = None
    """ISO-8601 timestamp of when the schedule was created."""

    day_of_month: Optional[int] = None
    """Day of the month, 1-31."""

    day_of_week: Optional[DigestDayOfWeek] = None
    """A day of the week. Accepted case-insensitively, returned lowercase."""

    days_of_week: Optional[List[DigestDayOfWeek]] = None

    disabled: Optional[bool] = None
    """Whether the schedule is disabled."""

    frequency: Optional[DigestFrequency] = None
    """Omitted for a stored schedule this enum cannot express.

    Those schedules never fire, but their `schedule_id` is still returned so the
    `/digests/*` endpoints remain reachable for them.
    """

    is_default: Optional[bool] = None
    """Whether this is the schedule recipients are placed on by default."""

    time: Optional[str] = None
    """24-hour local delivery time, `HH:MM`."""

    timezone: Optional[str] = None
    """IANA timezone the schedule is expressed in. Absent means UTC."""

    updated: Optional[str] = None
    """ISO-8601 timestamp of the last update."""
