# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ElementalContent"]


class ElementalContent(BaseModel):
    elements: List["ElementalNode"]

    version: str
    """For example, "2022-01-01" """

    brand: Optional[object] = None


from .elemental_node import ElementalNode
