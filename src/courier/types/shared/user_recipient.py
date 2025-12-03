# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .message_context import MessageContext
from .profile_preferences import ProfilePreferences

__all__ = ["UserRecipient"]


class UserRecipient(BaseModel):
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

    preferences: Optional[ProfilePreferences] = None

    tenant_id: Optional[str] = None
    """The id of the tenant the user is associated with."""

    user_id: Optional[str] = None
    """The user's unique identifier.

    Typically, this will match the user id of a user in your system.
    """
