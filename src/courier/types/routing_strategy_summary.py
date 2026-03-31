# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RoutingStrategySummary"]


class RoutingStrategySummary(BaseModel):
    """Routing strategy metadata returned in list responses.

    Does not include routing/channels/providers content.
    """

    id: str
    """The routing strategy ID (rs\\__ prefix)."""

    created: int
    """Epoch milliseconds when the strategy was created."""

    creator: str
    """User ID of the creator."""

    name: str
    """Human-readable name."""

    description: Optional[str] = None
    """Description of the routing strategy."""

    tags: Optional[List[str]] = None
    """Tags for categorization."""

    updated: Optional[int] = None
    """Epoch milliseconds of last update."""

    updater: Optional[str] = None
    """User ID of the last updater."""
