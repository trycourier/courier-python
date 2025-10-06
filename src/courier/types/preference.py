# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.rule import Rule
from .users.preference_status import PreferenceStatus
from .shared.channel_preference import ChannelPreference

__all__ = ["Preference"]


class Preference(BaseModel):
    status: PreferenceStatus

    channel_preferences: Optional[List[ChannelPreference]] = None

    rules: Optional[List[Rule]] = None

    source: Optional[Literal["subscription", "list", "recipient"]] = None
