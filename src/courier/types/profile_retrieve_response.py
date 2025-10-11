# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .shared.recipient_preferences import RecipientPreferences

__all__ = ["ProfileRetrieveResponse"]


class ProfileRetrieveResponse(BaseModel):
    profile: Dict[str, object]

    preferences: Optional[RecipientPreferences] = None
