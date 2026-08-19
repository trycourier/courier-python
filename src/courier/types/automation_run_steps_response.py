# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .automation_run_step import AutomationRunStep

__all__ = ["AutomationRunStepsResponse"]


class AutomationRunStepsResponse(BaseModel):
    """Every step of an Automation run. Not paginated."""

    steps: List[AutomationRunStep]
