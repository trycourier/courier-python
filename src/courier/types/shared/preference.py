# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .rule import Rule
from ..._models import BaseModel
from .channel_preference import ChannelPreference
from ..users.preference_status import PreferenceStatus

__all__ = ["Preference"]


class Preference(BaseModel):
    status: PreferenceStatus

    channel_preferences: Optional[List[ChannelPreference]] = None

    rules: Optional[List[Rule]] = None

    source: Optional[Literal["subscription", "list", "recipient"]] = None
