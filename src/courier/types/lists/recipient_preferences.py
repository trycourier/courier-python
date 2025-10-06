# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .notification_preference_details import NotificationPreferenceDetails

__all__ = ["RecipientPreferences"]


class RecipientPreferences(BaseModel):
    categories: Optional[Dict[str, NotificationPreferenceDetails]] = None

    notifications: Optional[Dict[str, NotificationPreferenceDetails]] = None
