# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .preference_param import PreferenceParam
from .message_context_param import MessageContextParam

__all__ = ["UserRecipientParam", "Preferences"]


class Preferences(TypedDict, total=False):
    notifications: Required[Dict[str, PreferenceParam]]

    categories: Optional[Dict[str, PreferenceParam]]

    template_id: Annotated[Optional[str], PropertyInfo(alias="templateId")]


class UserRecipientParam(TypedDict, total=False):
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
