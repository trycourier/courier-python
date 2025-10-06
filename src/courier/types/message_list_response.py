# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .paging import Paging
from .._models import BaseModel
from .message_details import MessageDetails

__all__ = ["MessageListResponse"]


class MessageListResponse(BaseModel):
    paging: Paging
    """Paging information for the result set."""

    results: List[MessageDetails]
    """An array of messages with their details."""
