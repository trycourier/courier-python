# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .notification_preference_details_param import NotificationPreferenceDetailsParam

__all__ = ["RecipientPreferencesParam"]


class RecipientPreferencesParam(TypedDict, total=False):
    categories: Optional[Dict[str, NotificationPreferenceDetailsParam]]

    notifications: Optional[Dict[str, NotificationPreferenceDetailsParam]]
