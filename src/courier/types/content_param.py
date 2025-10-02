# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ContentParam", "ElementalContent", "ElementalContentSugar"]


class ElementalContent(TypedDict, total=False):
    elements: Required[Iterable["ElementalNodeParam"]]

    version: Required[str]
    """For example, "2022-01-01" """

    brand: object


class ElementalContentSugar(TypedDict, total=False):
    body: Required[str]
    """The text content displayed in the notification."""

    title: Required[str]
    """The title to be displayed by supported channels i.e. push, email (as subject)"""


ContentParam: TypeAlias = Union[ElementalContent, ElementalContentSugar]

from .elemental_node_param import ElementalNodeParam
