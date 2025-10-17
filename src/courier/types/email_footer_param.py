# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailFooterParam"]


class EmailFooterParam(TypedDict, total=False):
    content: Optional[str]

    inherit_default: Annotated[Optional[bool], PropertyInfo(alias="inheritDefault")]
