# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .shared.message_channels import MessageChannels
from .shared.message_providers import MessageProviders

__all__ = ["RoutingStrategyGetResponse"]


class RoutingStrategyGetResponse(BaseModel):
    """Full routing strategy entity returned by GET."""

    id: str
    """The routing strategy ID (rs\\__ prefix)."""

    channels: MessageChannels
    """Per-channel delivery configuration. May be empty."""

    created: int
    """Epoch milliseconds when the strategy was created."""

    creator: str
    """User ID of the creator."""

    name: str
    """Human-readable name."""

    providers: MessageProviders
    """Per-provider delivery configuration. May be empty."""

    routing: "MessageRouting"
    """Routing tree defining channel selection method and order."""

    description: Optional[str] = None
    """Description of the routing strategy."""

    tags: Optional[List[str]] = None
    """Tags for categorization."""

    updated: Optional[int] = None
    """Epoch milliseconds of last update."""

    updater: Optional[str] = None
    """User ID of the last updater."""


from .shared.message_routing import MessageRouting
