# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.alignment import Alignment
from .elemental_channel_node import ElementalChannelNode
from .shared.elemental_base_node import ElementalBaseNode

__all__ = [
    "ElementalNode",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
    "UnionMember4Locales",
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


class UnionMember4Locales(BaseModel):
    content: str


class UnionMember4(BaseModel):
    action_id: Optional[str] = None
    """A unique id used to identify the action when it is executed."""

    align: Optional[Alignment] = None
    """The alignment of the action button. Defaults to "center"."""

    background_color: Optional[str] = None
    """The background color of the action button."""

    content: Optional[str] = None
    """The text content of the action shown to the user."""

    href: Optional[str] = None
    """The target URL of the action."""

    locales: Optional[Dict[str, UnionMember4Locales]] = None
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """

    style: Optional[Literal["button", "link"]] = None
    """Defaults to `button`."""

    type: Optional[Literal["action"]] = None


class UnionMember5(ElementalBaseNode):
    type: Optional[Literal["divider"]] = None


class UnionMember6(ElementalBaseNode):
    type: Optional[Literal["quote"]] = None


ElementalNode: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6
]
