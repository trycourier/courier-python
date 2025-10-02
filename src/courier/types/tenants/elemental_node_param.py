# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .elemental_group_node_param import ElementalGroupNodeParam
from .elemental_channel_node_param import ElementalChannelNodeParam

__all__ = [
    "ElementalNodeParam",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
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


class UnionMember2(ElementalChannelNodeParam, total=False):
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


_UnionMember4ReservedKeywords = TypedDict(
    "_UnionMember4ReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class UnionMember4(_UnionMember4ReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]

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


class UnionMember6(ElementalGroupNodeParam, total=False):
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
