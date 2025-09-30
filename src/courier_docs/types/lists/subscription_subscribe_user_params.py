# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .recipient_preferences_param import RecipientPreferencesParam

__all__ = ["SubscriptionSubscribeUserParams"]


class SubscriptionSubscribeUserParams(TypedDict, total=False):
    list_id: Required[str]

    preferences: Optional[RecipientPreferencesParam]
