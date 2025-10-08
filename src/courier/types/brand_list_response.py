# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.brand import Brand
from .shared.paging import Paging

__all__ = ["BrandListResponse"]


class BrandListResponse(BaseModel):
    paging: Paging

    results: List[Brand]
