# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .elemental_group_node import ElementalGroupNode
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
    "UnionMember7",
]


class UnionMember0(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["text"]] = None


class UnionMember1(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["meta"]] = None


class UnionMember2(ElementalChannelNode):
    type: Optional[Literal["channel"]] = None


class UnionMember3(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["image"]] = None


class UnionMember4(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["action"]] = None


class UnionMember5(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["divider"]] = None


class UnionMember6(ElementalGroupNode):
    type: Optional[Literal["group"]] = None


class UnionMember7(BaseModel):
    channels: Optional[List[str]] = None

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    ref: Optional[str] = None

    type: Optional[Literal["quote"]] = None


ElementalNode: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6, UnionMember7
]
