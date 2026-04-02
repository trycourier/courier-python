# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RoutingStrategyMutationResponse"]


class RoutingStrategyMutationResponse(BaseModel):
    """Response returned by create and replace operations."""

    id: str
    """The routing strategy ID (rs\\__ prefix)."""
