# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .locales import Locales
from ..shared.text_style import TextStyle
from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalTextNode"]


class ElementalTextNode(ElementalBaseNode, total=False):
    """Represents a body of text to be rendered inside of the notification."""

    align: Literal["left", "center", "right"]
    """Text alignment."""

    bold: Optional[str]
    """Apply bold to the text"""

    color: Optional[str]
    """Specifies the color of text. Can be any valid css color value"""

    content: str
    """The text content displayed in the notification.

    Either this field must be specified, or the elements field
    """

    font_size: Optional[str]
    """CSS px font size for this text block, e.g.

    `16px`. Overrides the size of the `text_style` preset. Email only.
    """

    format: Optional[Literal["markdown"]]

    italic: Optional[str]
    """Apply italics to the text"""

    line_height: Optional[str]
    """CSS line height for this text block, as a px value or a unitless multiplier,
    e.g.

    `24px` or `1.5`. Email only.
    """

    locales: Optional[Locales]
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """

    strikethrough: Optional[str]
    """Apply a strike through the text"""

    text_style: Optional[TextStyle]
    """Allows the text to be rendered as a heading level."""

    underline: Optional[str]
    """Apply an underline to the text"""
