# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .elemental_channel_node import ElementalChannelNode

__all__ = ["ElementalChannelNodeWithType"]


class ElementalChannelNodeWithType(ElementalChannelNode, total=False):
    type: Literal["channel"]
