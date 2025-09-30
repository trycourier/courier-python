# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .paging import Paging
from .._models import BaseModel

__all__ = ["AudienceListResponse"]


class AudienceListResponse(BaseModel):
    items: List["Audience"]

    paging: Paging


from .audience import Audience
