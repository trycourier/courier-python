# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.paging import Paging
from ..providers_catalog_entry import ProvidersCatalogEntry

__all__ = ["CatalogListResponse"]


class CatalogListResponse(BaseModel):
    """Paginated list of available provider types with their configuration schemas."""

    paging: Paging

    results: List[ProvidersCatalogEntry]
