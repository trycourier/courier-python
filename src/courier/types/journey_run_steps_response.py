# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .journey_run_step import JourneyRunStep

__all__ = ["JourneyRunStepsResponse"]


class JourneyRunStepsResponse(BaseModel):
    """Every step of a Journey run. Not paginated."""

    steps: List[JourneyRunStep]
