# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .brand_colors import BrandColors
from .brand_settings_email import BrandSettingsEmail
from .brand_settings_in_app import BrandSettingsInApp

__all__ = ["BrandSettings"]


class BrandSettings(TypedDict, total=False):
    colors: Optional[BrandColors]

    email: Optional[BrandSettingsEmail]

    inapp: Optional[BrandSettingsInApp]
