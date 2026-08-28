# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .elemental_quote_node import ElementalQuoteNode

__all__ = ["ElementalQuoteNodeWithType"]


class ElementalQuoteNodeWithType(ElementalQuoteNode, total=False):
    """Renders a quote block."""

    type: Literal["quote"]
