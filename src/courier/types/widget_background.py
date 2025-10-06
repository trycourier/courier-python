# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WidgetBackground"]


class WidgetBackground(BaseModel):
    bottom_color: Optional[str] = FieldInfo(alias="bottomColor", default=None)

    top_color: Optional[str] = FieldInfo(alias="topColor", default=None)
