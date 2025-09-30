# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BrandSettings", "Colors", "Email"]


class Colors(BaseModel):
    primary: Optional[str] = None

    secondary: Optional[str] = None

    tertiary: Optional[str] = None


class Email(BaseModel):
    footer: object

    header: object


class BrandSettings(BaseModel):
    colors: Optional[Colors] = None

    email: Optional[Email] = None

    inapp: Optional[object] = None
