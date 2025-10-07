# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .paging import Paging
from .._models import BaseModel
from .audience import Audience

__all__ = ["AudienceListResponse"]


class AudienceListResponse(BaseModel):
    items: List[Audience]

    paging: Paging
