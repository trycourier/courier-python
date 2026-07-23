# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from ..shared.preference_status import PreferenceStatus
from ..shared.channel_classification import ChannelClassification

__all__ = ["PreferenceUpdateOrCreateTopicParams", "Topic"]


class PreferenceUpdateOrCreateTopicParams(TypedDict, total=False):
    user_id: Required[str]

    topic: Required[Topic]

    tenant_id: Optional[str]
    """Update the preferences of a user for this specific tenant context."""


class Topic(TypedDict, total=False):
    status: Required[PreferenceStatus]
    """The subscription status to set: OPTED_IN or OPTED_OUT.

    REQUIRED is a topic-level default, not a user choice; the API rejects opting a
    user out of a REQUIRED topic.
    """

    custom_routing: Optional[List[ChannelClassification]]
    """The channels to deliver this topic on when has_custom_routing is true.

    One or more of: direct_message, email, push, sms, webhook, inbox.
    """

    has_custom_routing: Optional[bool]
    """
    Set to true to route this topic to the channels in custom_routing instead of the
    topic's default routing.
    """
