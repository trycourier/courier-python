# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .email_param import EmailParam
from .brand_colors_param import BrandColorsParam

__all__ = ["BrandSettingsParam"]


class BrandSettingsParam(TypedDict, total=False):
    colors: Optional[BrandColorsParam]

    email: Optional[EmailParam]

    inapp: object
