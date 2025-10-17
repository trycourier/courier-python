# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..check import Check
from ..._models import BaseModel

__all__ = ["CheckListResponse"]


class CheckListResponse(BaseModel):
    checks: List[Check]
