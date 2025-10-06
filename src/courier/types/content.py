# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .tenants.elemental_content import ElementalContent

__all__ = ["Content", "ElementalContentSugar"]


class ElementalContentSugar(BaseModel):
    body: str
    """The text content displayed in the notification."""

    title: str
    """Title/subject displayed by supported channels."""


Content: TypeAlias = Union[ElementalContentSugar, ElementalContent]
