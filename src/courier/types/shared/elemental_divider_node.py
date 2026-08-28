# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalDividerNode"]


class ElementalDividerNode(ElementalBaseNode):
    """Renders a dividing line between elements."""

    color: Optional[str] = None
    """The CSS color to render the line with. For example, `#fff`"""
