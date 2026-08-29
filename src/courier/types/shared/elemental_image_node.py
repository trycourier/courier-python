# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .alignment import Alignment
from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalImageNode"]


class ElementalImageNode(ElementalBaseNode):
    """Used to embed an image into the notification."""

    src: str
    """The source of the image."""

    align: Optional[Alignment] = None
    """The alignment of the image."""

    alt_text: Optional[str] = None
    """Alternate text for the image."""

    border_color: Optional[str] = None
    """CSS border color applied to the image. For example, `#ccc`"""

    border_size: Optional[str] = None
    """CSS border width applied to the image. For example, `1px`"""

    href: Optional[str] = None
    """A URL to link to when the image is clicked."""

    padding: Optional[str] = None
    """CSS padding applied around the image. For example, `10px`"""

    width: Optional[str] = None
    """CSS width properties to apply to the image. For example, 50px"""
