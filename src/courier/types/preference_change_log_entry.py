# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.preference_status import PreferenceStatus
from .preference_change_log_value import PreferenceChangeLogValue
from .shared.channel_classification import ChannelClassification

__all__ = ["PreferenceChangeLogEntry"]


class PreferenceChangeLogEntry(BaseModel):
    id: str
    """Unique identifier for this change."""

    custom_routing: List[ChannelClassification]
    """The channels chosen for this topic, present only when has_custom_routing is
    true.

    Empty otherwise.
    """

    has_custom_routing: bool
    """
    Whether specific delivery channels were chosen for this topic rather than the
    topic's default routing.
    """

    status: PreferenceStatus
    """The subscription status the change set."""

    timestamp: str
    """When the change was made, as an ISO-8601 date-time in UTC."""

    topic_id: str
    """The subscription topic the change applies to."""

    topic_name: str
    """The display name of that topic when the change was made."""

    user_id: str
    """The user whose preference changed."""

    previous: Optional[PreferenceChangeLogValue] = None
    """The value before this change, where it was recorded."""

    tenant_id: Optional[str] = None
    """The tenant context the change was made in.

    Absent when the user set the preference outside any tenant.
    """
