# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BrandColors"]


class BrandColors(BaseModel):
    primary: Optional[str] = None

    secondary: Optional[str] = None

    tertiary: Optional[str] = None
