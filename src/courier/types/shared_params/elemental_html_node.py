# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required

from .locales import Locales
from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalHTMLNode"]


class ElementalHTMLNode(ElementalBaseNode, total=False):
    """Raw HTML string inside an Elemental document.

    When rendering a message, this node is turned into output only for the email channel; for other channels it produces no blocks.
    """

    content: Required[str]
    """Raw HTML string to render inside the notification."""

    locales: Optional[Locales]
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """
