# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .elemental_image_node import ElementalImageNode

__all__ = ["ElementalImageNodeWithType"]


class ElementalImageNodeWithType(ElementalImageNode, total=False):
    """Used to embed an image into the notification."""

    type: Literal["image"]
