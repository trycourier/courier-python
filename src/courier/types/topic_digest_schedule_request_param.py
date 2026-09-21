# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .digest_frequency import DigestFrequency
from .digest_day_of_week import DigestDayOfWeek

__all__ = ["TopicDigestScheduleRequestParam"]


class TopicDigestScheduleRequestParam(TypedDict, total=False):
    """One delivery cadence for a topic's digest.

    Supply `schedule_id` to update an existing schedule in place; omit it and one is assigned and returned. The `schedules` array is a full replacement, so a stored schedule absent from it is deleted along with its delivery rule.

    Updating by `schedule_id` replaces that schedule rather than merging into it: any field you leave out is cleared. Two of those change delivery silently — an omitted `timezone` reverts the schedule to UTC, and an omitted `is_default` can leave the topic with no default schedule, which is what recipients who have not chosen one fall back to. Restate every field you want to keep.
    """

    frequency: Required[DigestFrequency]
    """How often a digest is delivered.

    `instant` delivers immediately without batching, and is the one value that takes
    no `time`.
    """

    day_of_month: int
    """Required when `frequency` is `monthly`."""

    day_of_week: DigestDayOfWeek
    """Required when `frequency` is `weekly`."""

    days_of_week: List[DigestDayOfWeek]
    """Required when `frequency` is `custom_days`."""

    disabled: bool
    """Whether the schedule is disabled."""

    is_default: bool
    """The schedule recipients are placed on when they have not chosen one.

    Set this explicitly rather than relying on array position.
    """

    schedule_id: str
    """Identifier of an existing schedule to update. Omit when creating a new one."""

    time: str
    """24-hour local delivery time, `HH:MM`.

    Required for every frequency except `instant`.
    """

    timezone: str
    """IANA timezone the `time` and day fields are expressed in, e.g.

    `America/New_York`. Absent means UTC. Delivery follows the same local wall-clock
    across daylight-saving changes.
    """
