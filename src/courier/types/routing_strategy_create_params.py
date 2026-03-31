# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared_params.message_channels import MessageChannels
from .shared_params.message_providers import MessageProviders

__all__ = ["RoutingStrategyCreateParams"]


class RoutingStrategyCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable name for the routing strategy."""

    routing: Required["MessageRouting"]
    """Routing tree defining channel selection method and order."""

    channels: Optional[MessageChannels]
    """Per-channel delivery configuration. Defaults to empty if omitted."""

    description: Optional[str]
    """Optional description of the routing strategy."""

    providers: Optional[MessageProviders]
    """Per-provider delivery configuration. Defaults to empty if omitted."""

    tags: Optional[SequenceNotStr[str]]
    """Optional tags for categorization."""


from .shared_params.message_routing import MessageRouting
