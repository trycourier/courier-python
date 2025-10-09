# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalDividerNodeWithType"]


class ElementalDividerNodeWithType(ElementalBaseNode, total=False):
    type: Literal["divider"]
