# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .logo import Logo
from .._models import BaseModel

__all__ = ["EmailHeader"]


class EmailHeader(BaseModel):
    logo: Logo

    bar_color: Optional[str] = FieldInfo(alias="barColor", default=None)

    inherit_default: Optional[bool] = FieldInfo(alias="inheritDefault", default=None)
