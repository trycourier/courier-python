# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .elemental_image_node import ElementalImageNode

__all__ = ["ElementalImageNodeWithType"]


class ElementalImageNodeWithType(ElementalImageNode):
    """Used to embed an image into the notification."""

    type: Optional[Literal["image"]] = None
