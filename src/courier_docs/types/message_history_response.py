# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["MessageHistoryResponse"]


class MessageHistoryResponse(BaseModel):
    results: List[Dict[str, object]]
