# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .elemental_text_node import ElementalTextNode

__all__ = ["ElementalTextNodeWithType"]


class ElementalTextNodeWithType(ElementalTextNode, total=False):
    """Represents a body of text to be rendered inside of the notification."""

    type: Literal["text"]
