# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared.alignment import Alignment
from .elemental_channel_node_param import ElementalChannelNodeParam
from .shared_params.elemental_base_node import ElementalBaseNode

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
]


class UnionMember0(ElementalBaseNode, total=False):
    type: Literal["text"]


class UnionMember1(ElementalBaseNode, total=False):
    type: Literal["meta"]


class UnionMember2(ElementalChannelNodeParam, total=False):
    type: Literal["channel"]


class UnionMember3(ElementalBaseNode, total=False):
    type: Literal["image"]


class UnionMember4Locales(TypedDict, total=False):
    content: Required[str]


class UnionMember4(TypedDict, total=False):
    action_id: Optional[str]
    """A unique id used to identify the action when it is executed."""

    align: Optional[Alignment]
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


class UnionMember5(ElementalBaseNode, total=False):
    type: Literal["divider"]


class UnionMember6(ElementalBaseNode, total=False):
    type: Literal["quote"]


ElementalNodeParam: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6
]
