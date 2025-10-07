# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .icons import Icons
from .._models import BaseModel
from .brand_colors import BrandColors
from .widget_background import WidgetBackground

__all__ = ["BrandSettingsInApp"]


class BrandSettingsInApp(BaseModel):
    colors: BrandColors

    icons: Icons

    widget_background: WidgetBackground = FieldInfo(alias="widgetBackground")

    border_radius: Optional[str] = FieldInfo(alias="borderRadius", default=None)

    disable_message_icon: Optional[bool] = FieldInfo(alias="disableMessageIcon", default=None)

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)

    placement: Optional[Literal["top", "bottom", "left", "right"]] = None
