# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .brand_colors import BrandColors
from .brand_settings_email import BrandSettingsEmail
from .brand_settings_in_app import BrandSettingsInApp

__all__ = ["BrandSettings"]


class BrandSettings(BaseModel):
    colors: Optional[BrandColors] = None

    email: Optional[BrandSettingsEmail] = None

    inapp: Optional[BrandSettingsInApp] = None
