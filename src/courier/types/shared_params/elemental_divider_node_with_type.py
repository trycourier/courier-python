# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .elemental_divider_node import ElementalDividerNode

__all__ = ["ElementalDividerNodeWithType"]


class ElementalDividerNodeWithType(ElementalDividerNode, total=False):
    """Renders a dividing line between elements."""

    type: Literal["divider"]
