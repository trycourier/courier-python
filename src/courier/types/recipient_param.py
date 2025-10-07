# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .message_context_param import MessageContextParam
from .shared_params.preference import Preference

__all__ = ["RecipientParam", "Preferences"]


class Preferences(TypedDict, total=False):
    notifications: Required[Dict[str, Preference]]

    categories: Optional[Dict[str, Preference]]

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
