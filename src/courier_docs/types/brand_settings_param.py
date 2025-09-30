# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BrandSettingsParam", "Colors", "Email"]


class Colors(TypedDict, total=False):
    primary: Optional[str]

    secondary: Optional[str]

    tertiary: Optional[str]


class Email(TypedDict, total=False):
    footer: Required[object]

    header: Required[object]


class BrandSettingsParam(TypedDict, total=False):
    colors: Optional[Colors]

    email: Optional[Email]

    inapp: object
