# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required

from ..shared.alignment import Alignment
from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalImageNode"]


class ElementalImageNode(ElementalBaseNode, total=False):
    """Used to embed an image into the notification."""

    src: Required[str]
    """The source of the image."""

    align: Optional[Alignment]
    """The alignment of the image."""

    alt_text: Optional[str]
    """Alternate text for the image."""

    border_color: Optional[str]
    """CSS border color applied to the image. For example, `#ccc`"""

    border_size: Optional[str]
    """CSS border width applied to the image. For example, `1px`"""

    href: Optional[str]
    """A URL to link to when the image is clicked."""

    padding: Optional[str]
    """CSS padding applied around the image. For example, `10px`"""

    width: Optional[str]
    """CSS width properties to apply to the image. For example, 50px"""
