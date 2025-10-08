# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

from .elemental_channel_node_param import ElementalChannelNodeParam
from .shared_params.elemental_base_node import ElementalBaseNode

__all__ = [
    "ElementalNodeParam",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
    "UnionMember5",
    "UnionMember6",
]


class UnionMember0(ElementalBaseNode, total=False):
    type: Literal["text"]


class UnionMember1(ElementalBaseNode, total=False):
    type: Literal["meta"]


class UnionMember2(ElementalChannelNodeParam, total=False):
    type: Literal["channel"]


class UnionMember3(ElementalBaseNode, total=False):
    type: Literal["image"]


class UnionMember4(ElementalBaseNode, total=False):
    type: Literal["action"]


class UnionMember5(ElementalBaseNode, total=False):
    type: Literal["divider"]


class UnionMember6(ElementalBaseNode, total=False):
    type: Literal["quote"]


ElementalNodeParam: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6
]
