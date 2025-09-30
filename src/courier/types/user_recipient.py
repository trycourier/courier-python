# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .message_context import MessageContext
from .users.preference_status import PreferenceStatus
from .tenants.default_preferences.channel_classification import ChannelClassification

__all__ = [
    "UserRecipient",
    "Preferences",
    "PreferencesNotifications",
    "PreferencesNotificationsChannelPreference",
    "PreferencesNotificationsRule",
    "PreferencesCategories",
    "PreferencesCategoriesChannelPreference",
    "PreferencesCategoriesRule",
]


class PreferencesNotificationsChannelPreference(BaseModel):
    channel: ChannelClassification


class PreferencesNotificationsRule(BaseModel):
    until: str

    start: Optional[str] = None


class PreferencesNotifications(BaseModel):
    status: PreferenceStatus

    channel_preferences: Optional[List[PreferencesNotificationsChannelPreference]] = None

    rules: Optional[List[PreferencesNotificationsRule]] = None

    source: Optional[Literal["subscription", "list", "recipient"]] = None


class PreferencesCategoriesChannelPreference(BaseModel):
    channel: ChannelClassification


class PreferencesCategoriesRule(BaseModel):
    until: str

    start: Optional[str] = None


class PreferencesCategories(BaseModel):
    status: PreferenceStatus

    channel_preferences: Optional[List[PreferencesCategoriesChannelPreference]] = None

    rules: Optional[List[PreferencesCategoriesRule]] = None

    source: Optional[Literal["subscription", "list", "recipient"]] = None


class Preferences(BaseModel):
    notifications: Dict[str, PreferencesNotifications]

    categories: Optional[Dict[str, PreferencesCategories]] = None

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)


class UserRecipient(BaseModel):
    account_id: Optional[str] = None
    """Use `tenant_id` instad."""

    context: Optional[MessageContext] = None
    """Context information such as tenant_id to send the notification with."""

    data: Optional[Dict[str, object]] = None

    email: Optional[str] = None

    locale: Optional[str] = None
    """The user's preferred ISO 639-1 language code."""

    phone_number: Optional[str] = None

    preferences: Optional[Preferences] = None

    tenant_id: Optional[str] = None
    """
    An id of a tenant,
    [see tenants api docs](https://www.courier.com/docs/reference/tenants). Will
    load brand, default preferences and any other base context data associated with
    this tenant.
    """

    user_id: Optional[str] = None
