# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared_params.rule import Rule
from .users.preference_status import PreferenceStatus
from .shared_params.channel_preference import ChannelPreference

__all__ = ["PreferenceParam"]


class PreferenceParam(TypedDict, total=False):
    status: Required[PreferenceStatus]

    channel_preferences: Optional[Iterable[ChannelPreference]]

    rules: Optional[Iterable[Rule]]

    source: Optional[Literal["subscription", "list", "recipient"]]
