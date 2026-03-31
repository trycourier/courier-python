# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.paging import Paging
from .routing_strategy_summary import RoutingStrategySummary

__all__ = ["RoutingStrategyListResponse"]


class RoutingStrategyListResponse(BaseModel):
    """Paginated list of routing strategy summaries."""

    paging: Paging

    results: List[RoutingStrategySummary]
