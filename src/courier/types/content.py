# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["Content", "ElementalContent", "ElementalContentSugar"]


class ElementalContent(BaseModel):
    elements: List["ElementalNode"]

    version: str
    """For example, "2022-01-01" """

    brand: Optional[object] = None


class ElementalContentSugar(BaseModel):
    body: str
    """The text content displayed in the notification."""

    title: str
    """The title to be displayed by supported channels i.e. push, email (as subject)"""


Content: TypeAlias = Union[ElementalContent, ElementalContentSugar]

from .elemental_node import ElementalNode
