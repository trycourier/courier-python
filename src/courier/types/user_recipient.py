# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .message_context import MessageContext
from .shared.preference import Preference

__all__ = ["UserRecipient", "Preferences"]


class Preferences(BaseModel):
    notifications: Dict[str, Preference]

    categories: Optional[Dict[str, Preference]] = None

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)


class UserRecipient(BaseModel):
    account_id: Optional[str] = None
    """Use `tenant_id` instead."""

    context: Optional[MessageContext] = None
    """Context such as tenant_id to send the notification with."""

    data: Optional[Dict[str, object]] = None

    email: Optional[str] = None

    locale: Optional[str] = None
    """The user's preferred ISO 639-1 language code."""

    phone_number: Optional[str] = None

    preferences: Optional[Preferences] = None

    tenant_id: Optional[str] = None
    """Tenant id. Will load brand, default preferences and base context data."""

    user_id: Optional[str] = None
