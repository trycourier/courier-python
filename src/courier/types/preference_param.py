# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PreferenceParam", "ChannelPreference", "Rule"]


class ChannelPreference(TypedDict, total=False):
    channel: Required[Literal["direct_message", "email", "push", "sms", "webhook", "inbox"]]


class Rule(TypedDict, total=False):
    until: Required[str]

    start: Optional[str]


class PreferenceParam(TypedDict, total=False):
    status: Required[Literal["OPTED_IN", "OPTED_OUT", "REQUIRED"]]

    channel_preferences: Optional[Iterable[ChannelPreference]]

    rules: Optional[Iterable[Rule]]

    source: Optional[Literal["subscription", "list", "recipient"]]
