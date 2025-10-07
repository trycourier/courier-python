# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["ListRecipient"]


class ListRecipient(BaseModel):
    data: Optional[Dict[str, object]] = None

    list_id: Optional[str] = None
