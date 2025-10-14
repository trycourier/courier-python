# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalActionNodeWithType"]


class ElementalActionNodeWithType(ElementalBaseNode):
    type: Optional[Literal["action"]] = None
