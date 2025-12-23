# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .audience_filter import AudienceFilter

__all__ = ["AudienceRecipient"]


class AudienceRecipient(BaseModel):
    """Send to all users in an audience"""

    audience_id: str
    """A unique identifier associated with an Audience.

    A message will be sent to each user in the audience.
    """

    data: Optional[Dict[str, object]] = None

    filters: Optional[List[AudienceFilter]] = None
