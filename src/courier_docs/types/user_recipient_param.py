# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .message_context_param import MessageContextParam
from .users.preference_status import PreferenceStatus
from .tenants.default_preferences.channel_classification import ChannelClassification

__all__ = [
    "UserRecipientParam",
    "Preferences",
    "PreferencesNotifications",
    "PreferencesNotificationsChannelPreference",
    "PreferencesNotificationsRule",
    "PreferencesCategories",
    "PreferencesCategoriesChannelPreference",
    "PreferencesCategoriesRule",
]


class PreferencesNotificationsChannelPreference(TypedDict, total=False):
    channel: Required[ChannelClassification]


class PreferencesNotificationsRule(TypedDict, total=False):
    until: Required[str]

    start: Optional[str]


class PreferencesNotifications(TypedDict, total=False):
    status: Required[PreferenceStatus]

    channel_preferences: Optional[Iterable[PreferencesNotificationsChannelPreference]]

    rules: Optional[Iterable[PreferencesNotificationsRule]]

    source: Optional[Literal["subscription", "list", "recipient"]]


class PreferencesCategoriesChannelPreference(TypedDict, total=False):
    channel: Required[ChannelClassification]


class PreferencesCategoriesRule(TypedDict, total=False):
    until: Required[str]

    start: Optional[str]


class PreferencesCategories(TypedDict, total=False):
    status: Required[PreferenceStatus]

    channel_preferences: Optional[Iterable[PreferencesCategoriesChannelPreference]]

    rules: Optional[Iterable[PreferencesCategoriesRule]]

    source: Optional[Literal["subscription", "list", "recipient"]]


class Preferences(TypedDict, total=False):
    notifications: Required[Dict[str, PreferencesNotifications]]

    categories: Optional[Dict[str, PreferencesCategories]]

    template_id: Annotated[Optional[str], PropertyInfo(alias="templateId")]


class UserRecipientParam(TypedDict, total=False):
    account_id: Optional[str]
    """Use `tenant_id` instad."""

    context: Optional[MessageContextParam]
    """Context information such as tenant_id to send the notification with."""

    data: Optional[Dict[str, object]]

    email: Optional[str]

    locale: Optional[str]
    """The user's preferred ISO 639-1 language code."""

    phone_number: Optional[str]

    preferences: Optional[Preferences]

    tenant_id: Optional[str]
    """
    An id of a tenant,
    [see tenants api docs](https://www.courier.com/docs/reference/tenants). Will
    load brand, default preferences and any other base context data associated with
    this tenant.
    """

    user_id: Optional[str]
