# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .email import Email
from .._models import BaseModel
from .brand_colors import BrandColors

__all__ = ["BrandSettings"]


class BrandSettings(BaseModel):
    colors: Optional[BrandColors] = None

    email: Optional[Email] = None

    inapp: Optional[object] = None
