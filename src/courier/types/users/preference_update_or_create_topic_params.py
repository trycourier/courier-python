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

    custom_routing: Optional[List[ChannelClassification]]
    """The Channels a user has chosen to receive notifications through for this topic"""

    has_custom_routing: Optional[bool]
