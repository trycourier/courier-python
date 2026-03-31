# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr
from .timeouts import Timeouts
from .channel_metadata import ChannelMetadata

__all__ = ["Channel"]

_ChannelReservedKeywords = TypedDict(
    "_ChannelReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class Channel(_ChannelReservedKeywords, total=False):
    brand_id: Optional[str]
    """Brand id used for rendering."""

    metadata: Optional[ChannelMetadata]

    override: Optional[Dict[str, object]]
    """Channel specific overrides."""

    providers: Optional[SequenceNotStr[str]]
    """Providers enabled for this channel."""

    routing_method: Optional[Literal["all", "single"]]
    """Defaults to `single`."""

    timeouts: Optional[Timeouts]
