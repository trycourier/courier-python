# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .alignment import Alignment
from .elemental_base_node import ElementalBaseNode

__all__ = [
    "ElementalContent",
    "Element",
    "ElementUnionMember0",
    "ElementUnionMember1",
    "ElementUnionMember2",
    "ElementUnionMember3",
    "ElementUnionMember4",
    "ElementUnionMember4Locales",
    "ElementUnionMember5",
    "ElementUnionMember6",
]


class ElementUnionMember0(ElementalBaseNode):
    type: Optional[Literal["text"]] = None


class ElementUnionMember1(ElementalBaseNode):
    type: Optional[Literal["meta"]] = None


class ElementUnionMember2(ElementalBaseNode):
    type: Optional[Literal["channel"]] = None


class ElementUnionMember3(ElementalBaseNode):
    type: Optional[Literal["image"]] = None


class ElementUnionMember4Locales(BaseModel):
    content: str


class ElementUnionMember4(BaseModel):
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

    locales: Optional[Dict[str, ElementUnionMember4Locales]] = None
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """

    style: Optional[Literal["button", "link"]] = None
    """Defaults to `button`."""

    type: Optional[Literal["action"]] = None


class ElementUnionMember5(ElementalBaseNode):
    type: Optional[Literal["divider"]] = None


class ElementUnionMember6(ElementalBaseNode):
    type: Optional[Literal["quote"]] = None


Element: TypeAlias = Union[
    ElementUnionMember0,
    ElementUnionMember1,
    ElementUnionMember2,
    ElementUnionMember3,
    ElementUnionMember4,
    ElementUnionMember5,
    ElementUnionMember6,
]


class ElementalContent(BaseModel):
    elements: List[Element]

    version: str
    """For example, "2022-01-01" """

    brand: Optional[str] = None
