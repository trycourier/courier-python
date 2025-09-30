# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from ..users.preference_status import PreferenceStatus
from ..tenants.default_preferences.channel_classification import ChannelClassification

__all__ = [
    "RecipientPreferences",
    "Categories",
    "CategoriesChannelPreference",
    "CategoriesRule",
    "Notifications",
    "NotificationsChannelPreference",
    "NotificationsRule",
]


class CategoriesChannelPreference(BaseModel):
    channel: ChannelClassification


class CategoriesRule(BaseModel):
    until: str

    start: Optional[str] = None


class Categories(BaseModel):
    status: PreferenceStatus

    channel_preferences: Optional[List[CategoriesChannelPreference]] = None

    rules: Optional[List[CategoriesRule]] = None


class NotificationsChannelPreference(BaseModel):
    channel: ChannelClassification


class NotificationsRule(BaseModel):
    until: str

    start: Optional[str] = None


class Notifications(BaseModel):
    status: PreferenceStatus

    channel_preferences: Optional[List[NotificationsChannelPreference]] = None

    rules: Optional[List[NotificationsRule]] = None


class RecipientPreferences(BaseModel):
    categories: Optional[Dict[str, Categories]] = None

    notifications: Optional[Dict[str, Notifications]] = None
