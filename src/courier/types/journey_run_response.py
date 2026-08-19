# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .journey_run import JourneyRun

__all__ = ["JourneyRunResponse"]


class JourneyRunResponse(BaseModel):
    """A single Journey run."""

    run: JourneyRun
    """One run of a Journey.

    `status` and `created_at` are absent on a small number of legacy runs stored
    without them.
    """
