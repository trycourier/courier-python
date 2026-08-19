# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .automation_run_list_item import AutomationRunListItem

__all__ = ["AutomationRunListResponse"]


class AutomationRunListResponse(BaseModel):
    """A page of Automation runs."""

    runs: List[AutomationRunListItem]

    next_cursor: Optional[str] = None
    """Pass back as `cursor` to fetch the next page. Absent on the last page."""
