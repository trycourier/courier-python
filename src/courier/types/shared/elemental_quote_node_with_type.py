# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .elemental_quote_node import ElementalQuoteNode

__all__ = ["ElementalQuoteNodeWithType"]


class ElementalQuoteNodeWithType(ElementalQuoteNode):
    """Renders a quote block."""

    type: Optional[Literal["quote"]] = None
