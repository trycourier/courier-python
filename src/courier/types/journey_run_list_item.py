# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["JourneyRunListItem"]


class JourneyRunListItem(BaseModel):
    """A Journey run as it appears in a list response, without `updated_at`."""

    run_id: str
    """A unique identifier representing the run."""

    source: List[str]
    """Internal provenance strings describing what started the run. Diagnostic only."""

    created_at: Optional[str] = None
    """When the run started, as an ISO 8601 timestamp."""

    status: Optional[str] = None
    """The state of the run. See `JourneyRun.status` for the values it takes."""

    template_id: Optional[str] = None
    """The id of the Journey this run belongs to."""
