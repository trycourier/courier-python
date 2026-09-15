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

    schedules: Required[Iterable[TopicDigestScheduleRequestParam]]
    """The cadences this digest delivers on.

    At least one is required: a digest with no schedule collects events into an
    instance that can never fire. Omitting the key on a replace leaves stored
    schedules untouched; sending `[]` is a `400`.
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

    trigger_empty: bool
    """Whether to deliver the digest even when nothing was collected."""
