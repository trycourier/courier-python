# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .shared.channel_classification import ChannelClassification

__all__ = ["PreferenceSectionCreateParams"]


class PreferenceSectionCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable name for the section."""

    has_custom_routing: Optional[bool]
    """Whether the section defines custom routing for its topics."""

    routing_options: Optional[List[ChannelClassification]]
    """Default channels for the section. Defaults to empty if omitted."""
