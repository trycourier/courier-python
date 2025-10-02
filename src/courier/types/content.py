# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["Content", "ElementalContentSugar"]


class ElementalContentSugar(BaseModel):
    body: str
    """The text content displayed in the notification."""

    title: str
    """The title to be displayed by supported channels i.e. push, email (as subject)"""


Content: TypeAlias = Union["ElementalContent", ElementalContentSugar]

from .tenants.elemental_content import ElementalContent
