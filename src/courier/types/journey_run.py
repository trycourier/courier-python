# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["JourneyRun"]


class JourneyRun(BaseModel):
    """One run of a Journey.

    `status` and `created_at` are absent on a small number of legacy runs stored without them.
    """

    run_id: str
    """A unique identifier representing the run."""

    source: List[str]
    """Internal provenance strings describing what started the run, e.g.

    `invoke/<journey_id>` or `segment/page/Pricing Page`. Diagnostic only — the
    format is unstable and should not be parsed.
    """

    created_at: Optional[str] = None
    """When the run started, as an ISO 8601 timestamp."""

    status: Optional[str] = None
    """
    The state of the run: `PROCESSING`, `PROCESSED`, `WAITING`, `CANCELED`, `ERROR`,
    `THROTTLED`, or `NOT PROCESSED`. Not an enum — new values have been added
    before.
    """

    template_id: Optional[str] = None
    """The id of the Journey this run belongs to."""

    updated_at: Optional[str] = None
    """When the run last changed state, as an ISO 8601 timestamp."""
