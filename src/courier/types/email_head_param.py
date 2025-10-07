# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailHeadParam"]


class EmailHeadParam(TypedDict, total=False):
    inherit_default: Required[Annotated[bool, PropertyInfo(alias="inheritDefault")]]

    content: Optional[str]
