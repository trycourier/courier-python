# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .alignment import Alignment
from .elemental_base_node_param import ElementalBaseNodeParam

__all__ = [
    "ElementalContentParam",
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


class ElementUnionMember0(ElementalBaseNodeParam, total=False):
    type: Literal["text"]


class ElementUnionMember1(ElementalBaseNodeParam, total=False):
    type: Literal["meta"]


class ElementUnionMember2(ElementalBaseNodeParam, total=False):
    type: Literal["channel"]


class ElementUnionMember3(ElementalBaseNodeParam, total=False):
    type: Literal["image"]


class ElementUnionMember4Locales(TypedDict, total=False):
    content: Required[str]


class ElementUnionMember4(TypedDict, total=False):
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

    locales: Optional[Dict[str, ElementUnionMember4Locales]]
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """

    style: Optional[Literal["button", "link"]]
    """Defaults to `button`."""

    type: Literal["action"]


class ElementUnionMember5(ElementalBaseNodeParam, total=False):
    type: Literal["divider"]


class ElementUnionMember6(ElementalBaseNodeParam, total=False):
    type: Literal["quote"]


Element: TypeAlias = Union[
    ElementUnionMember0,
    ElementUnionMember1,
    ElementUnionMember2,
    ElementUnionMember3,
    ElementUnionMember4,
    ElementUnionMember5,
    ElementUnionMember6,
]


class ElementalContentParam(TypedDict, total=False):
    elements: Required[Iterable[Element]]

    version: Required[str]
    """For example, "2022-01-01" """

    brand: Optional[str]
