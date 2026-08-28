# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .elemental_divider_node import ElementalDividerNode

__all__ = ["ElementalDividerNodeWithType"]


class ElementalDividerNodeWithType(ElementalDividerNode):
    """Renders a dividing line between elements."""

    type: Optional[Literal["divider"]] = None
