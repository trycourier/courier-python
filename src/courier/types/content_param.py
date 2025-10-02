# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ContentParam", "ElementalContentSugar"]


class ElementalContentSugar(TypedDict, total=False):
    body: Required[str]
    """The text content displayed in the notification."""

    title: Required[str]
    """The title to be displayed by supported channels i.e. push, email (as subject)"""


ContentParam: TypeAlias = Union["ElementalContentParam", ElementalContentSugar]

from .tenants.elemental_content_param import ElementalContentParam
