# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .notification_preference_details import NotificationPreferenceDetails

__all__ = ["RecipientPreferences"]


class RecipientPreferences(TypedDict, total=False):
    categories: Optional[Dict[str, NotificationPreferenceDetails]]

    notifications: Optional[Dict[str, NotificationPreferenceDetails]]
