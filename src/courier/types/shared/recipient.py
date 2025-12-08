# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .preference import Preference
from .message_context import MessageContext

__all__ = ["Recipient", "Preferences"]


class Preferences(BaseModel):
    notifications: Dict[str, Preference]

    categories: Optional[Dict[str, Preference]] = None

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)


class Recipient(BaseModel):
    account_id: Optional[str] = None
    """Deprecated - Use `tenant_id` instead."""

    context: Optional[MessageContext] = None
    """Context such as tenant_id to send the notification with."""

    data: Optional[Dict[str, object]] = None

    email: Optional[str] = None
    """The user's email address."""

    list_id: Optional[str] = None
    """The id of the list to send the message to."""

    locale: Optional[str] = None
    """The user's preferred ISO 639-1 language code."""

    phone_number: Optional[str] = None
    """The user's phone number."""

    preferences: Optional[Preferences] = None

    tenant_id: Optional[str] = None
    """The id of the tenant the user is associated with."""

    user_id: Optional[str] = None
    """The user's unique identifier.

    Typically, this will match the user id of a user in your system.
    """
