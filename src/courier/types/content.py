# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Content",
    "ElementalContent",
    "ElementalContentElement",
    "ElementalContentElementUnionMember0",
    "ElementalContentElementUnionMember1",
    "ElementalContentElementUnionMember2",
    "ElementalContentElementUnionMember3",
    "ElementalContentElementUnionMember4",
    "ElementalContentElementUnionMember5",
    "ElementalContentSugar",
]


class ElementalContentElementUnionMember0(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["text"]] = None


class ElementalContentElementUnionMember1(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["meta"]] = None


class ElementalContentElementUnionMember2(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["image"]] = None


class ElementalContentElementUnionMember3(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["action"]] = None


class ElementalContentElementUnionMember4(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class ElementalContentElementUnionMember5(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["quote"]] = None


ElementalContentElement: TypeAlias = Union[
    ElementalContentElementUnionMember0,
    ElementalContentElementUnionMember1,
    ElementalContentElementUnionMember2,
    ElementalContentElementUnionMember3,
    ElementalContentElementUnionMember4,
    ElementalContentElementUnionMember5,
]


class ElementalContent(BaseModel):
    elements: List[ElementalContentElement]

    version: str
    """For example, "2022-01-01" """

    brand: Optional[object] = None


class ElementalContentSugar(BaseModel):
    body: str
    """The text content displayed in the notification."""

    title: str
    """The title to be displayed by supported channels i.e. push, email (as subject)"""


Content: TypeAlias = Union[ElementalContent, ElementalContentSugar]
