# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .list_filter import ListFilter

__all__ = ["ListRecipient"]


class ListRecipient(BaseModel):
    """Send to all users in a specific list"""

    data: Optional[Dict[str, object]] = None

    filters: Optional[List[ListFilter]] = None

    list_id: Optional[str] = None
