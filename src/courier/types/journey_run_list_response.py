# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .journey_run_list_item import JourneyRunListItem

__all__ = ["JourneyRunListResponse"]


class JourneyRunListResponse(BaseModel):
    """A page of Journey runs."""

    runs: List[JourneyRunListItem]

    next_cursor: Optional[str] = None
    """Pass back as `cursor` to fetch the next page. Absent on the last page."""

    prev_cursor: Optional[str] = None
    """Pass back as `cursor` to fetch the previous page. Absent on the first page."""
