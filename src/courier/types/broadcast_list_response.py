# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .broadcast import Broadcast
from .shared.paging import Paging

__all__ = ["BroadcastListResponse"]


class BroadcastListResponse(BaseModel):
    """Paginated list of broadcasts."""

    paging: Paging

    results: List[Broadcast]
