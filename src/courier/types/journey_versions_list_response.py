# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.paging import Paging
from .journey_version_item import JourneyVersionItem

__all__ = ["JourneyVersionsListResponse"]


class JourneyVersionsListResponse(BaseModel):
    """Paged list of published journey versions, most recent first."""

    paging: Paging

    results: List[JourneyVersionItem]
