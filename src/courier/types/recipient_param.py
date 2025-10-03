# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .message_context_param import MessageContextParam

__all__ = [
    "RecipientParam",
    "Preferences",
    "PreferencesNotifications",
    "PreferencesNotificationsChannelPreference",
    "PreferencesNotificationsRule",
    "PreferencesCategories",
    "PreferencesCategoriesChannelPreference",
    "PreferencesCategoriesRule",
]


class PreferencesNotificationsChannelPreference(TypedDict, total=False):
    channel: Required[Literal["direct_message", "email", "push", "sms", "webhook", "inbox"]]


class PreferencesNotificationsRule(TypedDict, total=False):
    until: Required[str]

    start: Optional[str]


class PreferencesNotifications(TypedDict, total=False):
    status: Required[Literal["OPTED_IN", "OPTED_OUT", "REQUIRED"]]

    channel_preferences: Optional[Iterable[PreferencesNotificationsChannelPreference]]

    rules: Optional[Iterable[PreferencesNotificationsRule]]

    source: Optional[Literal["subscription", "list", "recipient"]]


class PreferencesCategoriesChannelPreference(TypedDict, total=False):
    channel: Required[Literal["direct_message", "email", "push", "sms", "webhook", "inbox"]]


class PreferencesCategoriesRule(TypedDict, total=False):
    until: Required[str]

    start: Optional[str]


class PreferencesCategories(TypedDict, total=False):
    status: Required[Literal["OPTED_IN", "OPTED_OUT", "REQUIRED"]]

    channel_preferences: Optional[Iterable[PreferencesCategoriesChannelPreference]]

    rules: Optional[Iterable[PreferencesCategoriesRule]]

    source: Optional[Literal["subscription", "list", "recipient"]]


class Preferences(TypedDict, total=False):
    notifications: Required[Dict[str, PreferencesNotifications]]

    categories: Optional[Dict[str, PreferencesCategories]]

    template_id: Annotated[Optional[str], PropertyInfo(alias="templateId")]


class RecipientParam(TypedDict, total=False):
    account_id: Optional[str]
    """Use `tenant_id` instead."""

    context: Optional[MessageContextParam]
    """Context such as tenant_id to send the notification with."""

    data: Optional[Dict[str, object]]

    email: Optional[str]

    locale: Optional[str]
    """The user's preferred ISO 639-1 language code."""

    phone_number: Optional[str]

    preferences: Optional[Preferences]

    tenant_id: Optional[str]
    """Tenant id. Will load brand, default preferences and base context data."""

    user_id: Optional[str]
