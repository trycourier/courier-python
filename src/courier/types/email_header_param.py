# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .logo_param import LogoParam

__all__ = ["EmailHeaderParam"]


class EmailHeaderParam(TypedDict, total=False):
    logo: Required[LogoParam]

    bar_color: Annotated[Optional[str], PropertyInfo(alias="barColor")]

    inherit_default: Annotated[Optional[bool], PropertyInfo(alias="inheritDefault")]
