# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..topic_digest_category_param import TopicDigestCategoryParam
from ..shared.channel_classification import ChannelClassification
from ..topic_digest_schedule_request_param import TopicDigestScheduleRequestParam

__all__ = ["TopicCreateParams", "Digest"]


class TopicCreateParams(TypedDict, total=False):
    default_status: Required[Literal["OPTED_OUT", "OPTED_IN", "REQUIRED"]]
    """The default subscription status applied when a recipient has not set their own."""

    name: Required[str]
    """Human-readable name for the preference topic."""

    allowed_preferences: Optional[List[Literal["snooze", "channel_preferences"]]]
    """Preference controls a recipient may customize for this topic.

    Defaults to empty if omitted.
    """

    description: Optional[str]
    """Optional description shown under the topic on the hosted preferences page."""

    digest: Optional[Digest]
    """
    A topic's digest, as supplied when the topic itself is created: the template
    that renders it, the cadences it delivers on, and how collected events are
    retained.

    Identical to `TopicDigestRequest`, which a replace uses, except that `schedules`
    is required — a topic being created has no stored schedules for an absent key to
    leave alone.

    Send `null` for the whole object to turn a digest off, which unlinks the
    template and removes its schedules. There is no `enabled` flag, and
    `schedules: []` is rejected, because both states are un-deliverable rather than
    merely off.
    """

    include_unsubscribe_header: Optional[bool]
    """Whether to include a list-unsubscribe header on emails for this topic."""

    routing_options: Optional[List[ChannelClassification]]
    """Default channels delivered for this topic. Defaults to empty if omitted."""

    topic_data: Optional[Dict[str, object]]
    """Arbitrary metadata associated with the topic."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]


class Digest(TypedDict, total=False):
    """
    A topic's digest, as supplied when the topic itself is created: the template that renders it, the cadences it delivers on, and how collected events are retained.

    Identical to `TopicDigestRequest`, which a replace uses, except that `schedules` is required — a topic being created has no stored schedules for an absent key to leave alone.

    Send `null` for the whole object to turn a digest off, which unlinks the template and removes its schedules. There is no `enabled` flag, and `schedules: []` is rejected, because both states are un-deliverable rather than merely off.
    """

    schedules: Required[Iterable[TopicDigestScheduleRequestParam]]
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
