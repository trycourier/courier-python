# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ContentParam",
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

_ElementalContentElementUnionMember0ReservedKeywords = TypedDict(
    "_ElementalContentElementUnionMember0ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalContentElementUnionMember0(_ElementalContentElementUnionMember0ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["text"]


_ElementalContentElementUnionMember1ReservedKeywords = TypedDict(
    "_ElementalContentElementUnionMember1ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalContentElementUnionMember1(_ElementalContentElementUnionMember1ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["meta"]


_ElementalContentElementUnionMember2ReservedKeywords = TypedDict(
    "_ElementalContentElementUnionMember2ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalContentElementUnionMember2(_ElementalContentElementUnionMember2ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["image"]


_ElementalContentElementUnionMember3ReservedKeywords = TypedDict(
    "_ElementalContentElementUnionMember3ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalContentElementUnionMember3(_ElementalContentElementUnionMember3ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["action"]


_ElementalContentElementUnionMember4ReservedKeywords = TypedDict(
    "_ElementalContentElementUnionMember4ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalContentElementUnionMember4(_ElementalContentElementUnionMember4ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["divider"]


_ElementalContentElementUnionMember5ReservedKeywords = TypedDict(
    "_ElementalContentElementUnionMember5ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalContentElementUnionMember5(_ElementalContentElementUnionMember5ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["quote"]


ElementalContentElement: TypeAlias = Union[
    ElementalContentElementUnionMember0,
    ElementalContentElementUnionMember1,
    ElementalContentElementUnionMember2,
    ElementalContentElementUnionMember3,
    ElementalContentElementUnionMember4,
    ElementalContentElementUnionMember5,
]


class ElementalContent(TypedDict, total=False):
    elements: Required[Iterable[ElementalContentElement]]

    version: Required[str]
    """For example, "2022-01-01" """

    brand: object


class ElementalContentSugar(TypedDict, total=False):
    body: Required[str]
    """The text content displayed in the notification."""

    title: Required[str]
    """The title to be displayed by supported channels i.e. push, email (as subject)"""


ContentParam: TypeAlias = Union[ElementalContent, ElementalContentSugar]
