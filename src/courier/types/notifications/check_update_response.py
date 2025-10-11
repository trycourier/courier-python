# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.check import Check

__all__ = ["CheckUpdateResponse"]


class CheckUpdateResponse(BaseModel):
    checks: List[Check]
