# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..topic_digest_request_param import TopicDigestRequestParam
from ..shared.channel_classification import ChannelClassification

__all__ = ["TopicCreateParams"]


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

    digest: Optional[TopicDigestRequestParam]
    """
    A topic's digest configuration: the template that renders it, the cadences it
    delivers on, and how collected events are retained.

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
