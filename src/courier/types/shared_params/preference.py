# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .rule import Rule
from .channel_preference import ChannelPreference
from ..shared.preference_status import PreferenceStatus

__all__ = ["Preference"]


class Preference(TypedDict, total=False):
    status: Required[PreferenceStatus]

    channel_preferences: Optional[Iterable[ChannelPreference]]

    rules: Optional[Iterable[Rule]]

    source: Optional[Literal["subscription", "list", "recipient"]]
