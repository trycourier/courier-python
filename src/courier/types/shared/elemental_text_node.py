# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .locales import Locales
from .text_style import TextStyle
from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalTextNode"]


class ElementalTextNode(ElementalBaseNode):
    """Represents a body of text to be rendered inside of the notification."""

    align: Optional[Literal["left", "center", "right"]] = None
    """Text alignment."""

    bold: Optional[str] = None
    """Apply bold to the text"""

    color: Optional[str] = None
    """Specifies the color of text. Can be any valid css color value"""

    content: Optional[str] = None
    """The text content displayed in the notification.

    Either this field must be specified, or the elements field
    """

    font_size: Optional[str] = None
    """CSS px font size for this text block, e.g.

    `16px`. Overrides the size of the `text_style` preset. Email only.
    """

    format: Optional[Literal["markdown"]] = None

    italic: Optional[str] = None
    """Apply italics to the text"""

    line_height: Optional[str] = None
    """CSS line height for this text block, as a px value or a unitless multiplier,
    e.g.

    `24px` or `1.5`. Email only.
    """

    locales: Optional[Locales] = None
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """

    strikethrough: Optional[str] = None
    """Apply a strike through the text"""

    text_style: Optional[TextStyle] = None
    """Allows the text to be rendered as a heading level."""

    underline: Optional[str] = None
    """Apply an underline to the text"""
