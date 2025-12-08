# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .preference import Preference
from .message_context import MessageContext

__all__ = ["Recipient", "Preferences"]


class Preferences(TypedDict, total=False):
    notifications: Required[Dict[str, Preference]]

    categories: Optional[Dict[str, Preference]]

    template_id: Annotated[Optional[str], PropertyInfo(alias="templateId")]


class Recipient(TypedDict, total=False):
    account_id: Optional[str]
    """Deprecated - Use `tenant_id` instead."""

    context: Optional[MessageContext]
    """Context such as tenant_id to send the notification with."""

    data: Optional[Dict[str, object]]

    email: Optional[str]
    """The user's email address."""

    list_id: Optional[str]
    """The id of the list to send the message to."""

    locale: Optional[str]
    """The user's preferred ISO 639-1 language code."""

    phone_number: Optional[str]
    """The user's phone number."""

    preferences: Optional[Preferences]

    tenant_id: Optional[str]
    """The id of the tenant the user is associated with."""

    user_id: Optional[str]
    """The user's unique identifier.

    Typically, this will match the user id of a user in your system.
    """
