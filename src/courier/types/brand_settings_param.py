# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .brand_colors_param import BrandColorsParam
from .brand_settings_email_param import BrandSettingsEmailParam
from .brand_settings_in_app_param import BrandSettingsInAppParam

__all__ = ["BrandSettingsParam"]


class BrandSettingsParam(TypedDict, total=False):
    colors: Optional[BrandColorsParam]

    email: Optional[BrandSettingsEmailParam]

    inapp: Optional[BrandSettingsInAppParam]
