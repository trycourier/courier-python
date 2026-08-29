# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .locales import Locales
from .alignment import Alignment
from .text_style import TextStyle
from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalQuoteNode"]


class ElementalQuoteNode(ElementalBaseNode):
    """Renders a quote block."""

    content: str
    """The text value of the quote."""

    align: Optional[Alignment] = None
    """Alignment of the quote."""

    border_color: Optional[str] = None
    """CSS border color property. For example, `#fff`"""

    font_size: Optional[str] = None
    """CSS px font size for this quote block, e.g.

    `16px`. Overrides the size of the `text_style` preset. Email only.
    """

    line_height: Optional[str] = None
    """
    CSS line height for this quote block, as a px value or a unitless multiplier,
    e.g. `24px` or `1.5`. Email only.
    """

    locales: Optional[Locales] = None
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """

    text_style: Optional[TextStyle] = None
