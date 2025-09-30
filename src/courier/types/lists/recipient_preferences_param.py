# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..users.preference_status import PreferenceStatus
from ..tenants.default_preferences.channel_classification import ChannelClassification

__all__ = [
    "RecipientPreferencesParam",
    "Categories",
    "CategoriesChannelPreference",
    "CategoriesRule",
    "Notifications",
    "NotificationsChannelPreference",
    "NotificationsRule",
]


class CategoriesChannelPreference(TypedDict, total=False):
    channel: Required[ChannelClassification]


class CategoriesRule(TypedDict, total=False):
    until: Required[str]

    start: Optional[str]


class Categories(TypedDict, total=False):
    status: Required[PreferenceStatus]

    channel_preferences: Optional[Iterable[CategoriesChannelPreference]]

    rules: Optional[Iterable[CategoriesRule]]


class NotificationsChannelPreference(TypedDict, total=False):
    channel: Required[ChannelClassification]


class NotificationsRule(TypedDict, total=False):
    until: Required[str]

    start: Optional[str]


class Notifications(TypedDict, total=False):
    status: Required[PreferenceStatus]

    channel_preferences: Optional[Iterable[NotificationsChannelPreference]]

    rules: Optional[Iterable[NotificationsRule]]


class RecipientPreferencesParam(TypedDict, total=False):
    categories: Optional[Dict[str, Categories]]

    notifications: Optional[Dict[str, Notifications]]
