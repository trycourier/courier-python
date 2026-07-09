# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

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

    include_unsubscribe_header: Optional[bool]
    """Whether to include a list-unsubscribe header on emails for this topic."""

    routing_options: Optional[List[ChannelClassification]]
    """Default channels delivered for this topic. Defaults to empty if omitted."""

    topic_data: Optional[Dict[str, object]]
    """Arbitrary metadata associated with the topic."""
