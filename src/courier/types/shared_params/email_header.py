# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .logo import Logo
from ..._utils import PropertyInfo

__all__ = ["EmailHeader"]


class EmailHeader(TypedDict, total=False):
    logo: Required[Logo]

    bar_color: Annotated[Optional[str], PropertyInfo(alias="barColor")]

    inherit_default: Annotated[Optional[bool], PropertyInfo(alias="inheritDefault")]
