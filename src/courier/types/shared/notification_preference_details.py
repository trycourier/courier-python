# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .rule import Rule
from ..._models import BaseModel
from .preference_status import PreferenceStatus
from .channel_preference import ChannelPreference

__all__ = ["NotificationPreferenceDetails"]


class NotificationPreferenceDetails(BaseModel):
    status: PreferenceStatus

    channel_preferences: Optional[List[ChannelPreference]] = None

    rules: Optional[List[Rule]] = None
