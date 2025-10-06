# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ElementalNodeParam",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
    "UnionMember4Locales",
    "UnionMember5",
    "UnionMember6",
    "UnionMember7",
]

_UnionMember0ReservedKeywords = TypedDict(
    "_UnionMember0ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class UnionMember0(_UnionMember0ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["text"]


_UnionMember1ReservedKeywords = TypedDict(
    "_UnionMember1ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class UnionMember1(_UnionMember1ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["meta"]


_UnionMember2ReservedKeywords = TypedDict(
    "_UnionMember2ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class UnionMember2(_UnionMember2ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["channel"]


_UnionMember3ReservedKeywords = TypedDict(
    "_UnionMember3ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class UnionMember3(_UnionMember3ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["image"]


class UnionMember4Locales(TypedDict, total=False):
    content: Required[str]


class UnionMember4(TypedDict, total=False):
    action_id: Optional[str]
    """A unique id used to identify the action when it is executed."""

    align: Optional[Literal["center", "left", "right", "full"]]
    """The alignment of the action button. Defaults to "center"."""

    background_color: Optional[str]
    """The background color of the action button."""

    content: str
    """The text content of the action shown to the user."""

    href: str
    """The target URL of the action."""

    locales: Optional[Dict[str, UnionMember4Locales]]
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """

    style: Optional[Literal["button", "link"]]
    """Defaults to `button`."""

    type: Literal["action"]


_UnionMember5ReservedKeywords = TypedDict(
    "_UnionMember5ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class UnionMember5(_UnionMember5ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["divider"]


_UnionMember6ReservedKeywords = TypedDict(
    "_UnionMember6ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class UnionMember6(_UnionMember6ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["group"]


_UnionMember7ReservedKeywords = TypedDict(
    "_UnionMember7ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class UnionMember7(_UnionMember7ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

    type: Literal["quote"]


ElementalNodeParam: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6, UnionMember7
]
