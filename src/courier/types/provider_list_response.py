# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .provider import Provider
from .shared.paging import Paging

__all__ = ["ProviderListResponse"]


class ProviderListResponse(BaseModel):
    """Paginated list of provider configurations."""

    paging: Paging

    results: List[Provider]
