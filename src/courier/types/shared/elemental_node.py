# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .elemental_base_node import ElementalBaseNode
from .elemental_channel_node import ElementalChannelNode

__all__ = [
    "ElementalNode",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
    "UnionMember5",
    "UnionMember6",
]


class UnionMember0(ElementalBaseNode):
    type: Optional[Literal["text"]] = None


class UnionMember1(ElementalBaseNode):
    type: Optional[Literal["meta"]] = None


class UnionMember2(ElementalChannelNode):
    type: Optional[Literal["channel"]] = None


class UnionMember3(ElementalBaseNode):
    type: Optional[Literal["image"]] = None


class UnionMember4(ElementalBaseNode):
    type: Optional[Literal["action"]] = None


class UnionMember5(ElementalBaseNode):
    type: Optional[Literal["divider"]] = None


class UnionMember6(ElementalBaseNode):
    type: Optional[Literal["quote"]] = None


ElementalNode: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6
]
