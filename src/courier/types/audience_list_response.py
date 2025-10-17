# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .audience import Audience
from .shared.paging import Paging

__all__ = ["AudienceListResponse"]


class AudienceListResponse(BaseModel):
    items: List[Audience]

    paging: Paging
