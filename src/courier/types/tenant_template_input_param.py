# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .shared_params.utm import Utm
from .shared_params.elemental_content import ElementalContent

__all__ = [
    "TenantTemplateInputParam",
    "Channels",
    "ChannelsMetadata",
    "ChannelsTimeouts",
    "Providers",
    "ProvidersMetadata",
]


class ChannelsMetadata(TypedDict, total=False):
    utm: Optional[Utm]


class ChannelsTimeouts(TypedDict, total=False):
    channel: Optional[int]

    provider: Optional[int]


_ChannelsReservedKeywords = TypedDict(
    "_ChannelsReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class Channels(_ChannelsReservedKeywords, total=False):
    brand_id: Optional[str]
    """Brand id used for rendering."""

    metadata: Optional[ChannelsMetadata]

    override: Optional[Dict[str, object]]
    """Channel specific overrides."""

    providers: Optional[SequenceNotStr[str]]
    """Providers enabled for this channel."""

    routing_method: Optional[Literal["all", "single"]]
    """Defaults to `single`."""

    timeouts: Optional[ChannelsTimeouts]


class ProvidersMetadata(TypedDict, total=False):
    utm: Optional[Utm]


_ProvidersReservedKeywords = TypedDict(
    "_ProvidersReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class Providers(_ProvidersReservedKeywords, total=False):
    metadata: Optional[ProvidersMetadata]

    override: Optional[Dict[str, object]]
    """Provider-specific overrides."""

    timeouts: Optional[int]


class TenantTemplateInputParam(TypedDict, total=False):
    """Template configuration for creating or updating a tenant notification template"""

    content: Required[ElementalContent]
    """
    Template content configuration including blocks, elements, and message structure
    """

    channels: Dict[str, Channels]
    """Channel-specific delivery configuration (email, SMS, push, etc.)"""

    providers: Dict[str, Providers]
    """
    Provider-specific delivery configuration for routing to specific email/SMS
    providers
    """

    routing: "MessageRouting"
    """Message routing configuration for multi-channel delivery strategies"""


from .shared_params.message_routing import MessageRouting
