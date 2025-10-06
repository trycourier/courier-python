# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .tenants.elemental_content_param import ElementalContentParam

__all__ = ["ContentParam", "ElementalContentSugar"]


class ElementalContentSugar(TypedDict, total=False):
    body: Required[str]
    """The text content displayed in the notification."""

    title: Required[str]
    """Title/subject displayed by supported channels."""


ContentParam: TypeAlias = Union[ElementalContentSugar, ElementalContentParam]
