# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .elemental_channel_node import ElementalChannelNode

__all__ = ["ElementalChannelNodeWithType"]


class ElementalChannelNodeWithType(ElementalChannelNode):
    type: Optional[Literal["channel"]] = None
