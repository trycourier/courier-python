# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required

from .locales import Locales
from ..shared.alignment import Alignment
from ..shared.text_style import TextStyle
from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalQuoteNode"]


class ElementalQuoteNode(ElementalBaseNode, total=False):
    """Renders a quote block."""

    content: Required[str]
    """The text value of the quote."""

    align: Optional[Alignment]
    """Alignment of the quote."""

    border_color: Optional[str]
    """CSS border color property. For example, `#fff`"""

    font_size: Optional[str]
    """CSS px font size for this quote block, e.g.

    `16px`. Overrides the size of the `text_style` preset. Email only.
    """

    line_height: Optional[str]
    """
    CSS line height for this quote block, as a px value or a unitless multiplier,
    e.g. `24px` or `1.5`. Email only.
    """

    locales: Optional[Locales]
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """

    text_style: TextStyle
