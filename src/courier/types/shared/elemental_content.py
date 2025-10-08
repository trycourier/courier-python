# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .elemental_node import ElementalNode

__all__ = ["ElementalContent"]


class ElementalContent(BaseModel):
    elements: List[ElementalNode]

    version: str
    """For example, "2022-01-01" """

    brand: Optional[str] = None
