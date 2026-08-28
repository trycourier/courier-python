# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .elemental_html_node import ElementalHTMLNode

__all__ = ["ElementalHTMLNodeWithType"]


class ElementalHTMLNodeWithType(ElementalHTMLNode):
    """Raw HTML string inside an Elemental document.

    When rendering a message, this node is turned into output only for the email channel; for other channels it produces no blocks.
    """

    type: Optional[Literal["html"]] = None
