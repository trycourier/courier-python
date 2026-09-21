# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .topic_digest_category_param import TopicDigestCategoryParam
from .topic_digest_schedule_request_param import TopicDigestScheduleRequestParam

__all__ = ["TopicDigestRequestParam"]


class TopicDigestRequestParam(TypedDict, total=False):
    """
    A topic's digest configuration: the template that renders it, the cadences it delivers on, and how collected events are retained.

    Send `null` for the whole object to turn a digest off, which unlinks the template and removes its schedules. There is no `enabled` flag, and `schedules: []` is rejected, because both states are un-deliverable rather than merely off.
    """

    template_id: Required[str]
    """The notification template that renders the digest.

    A digest with no template collects nothing, so this is required.
    """

    audience_id: str
    """Optional audience the digest is scoped to."""

    categories: Iterable[TopicDigestCategoryParam]
    """Retention rules per category key.

    Defaults to a single `digest` category retaining `FIRST`.
    """

    schedules: Iterable[TopicDigestScheduleRequestParam]
    """The cadences this digest delivers on.

    The array replaces the stored schedules wholesale, so a schedule you leave out
    of it is deleted along with its delivery rule. Omit the key entirely to leave
    the stored schedules untouched — useful for changing `template_id` or
    `categories` without restating every schedule.

    A digest must end up with at least one schedule, because one with none collects
    events into an instance that can never fire. So sending `[]` is always a `400`,
    and so is omitting the key on a topic that has no schedules stored yet.

    On **create** the key is required outright: a topic being created has nothing
    stored to leave alone, and the topic row is written before its digest, so
    rejecting it any later would leave the topic behind and let a retry duplicate
    it.
    """

    trigger_empty: bool
    """Whether to deliver the digest even when nothing was collected."""
