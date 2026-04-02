# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared_params.message_channels import MessageChannels
from .shared_params.message_providers import MessageProviders

__all__ = ["RoutingStrategyReplaceParams"]


class RoutingStrategyReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable name for the routing strategy."""

    routing: Required["MessageRouting"]
    """Routing tree defining channel selection method and order."""

    channels: Optional[MessageChannels]
    """Per-channel delivery configuration. Omit to clear."""

    description: Optional[str]
    """Optional description. Omit or null to clear."""

    providers: Optional[MessageProviders]
    """Per-provider delivery configuration. Omit to clear."""

    tags: Optional[SequenceNotStr[str]]
    """Optional tags. Omit or null to clear."""


from .shared_params.message_routing import MessageRouting
