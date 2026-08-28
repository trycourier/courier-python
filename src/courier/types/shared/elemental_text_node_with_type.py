# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .elemental_text_node import ElementalTextNode

__all__ = ["ElementalTextNodeWithType"]


class ElementalTextNodeWithType(ElementalTextNode):
    """Represents a body of text to be rendered inside of the notification."""

    type: Optional[Literal["text"]] = None
