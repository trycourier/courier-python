# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ElementalGroupNode"]


class ElementalGroupNode(BaseModel):
    elements: List["ElementalNode"]
    """Sub elements to render."""

    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None


from .elemental_node import ElementalNode
