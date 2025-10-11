# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .icons import Icons
from ..._utils import PropertyInfo
from .brand_colors import BrandColors
from .widget_background import WidgetBackground

__all__ = ["BrandSettingsInApp"]


class BrandSettingsInApp(TypedDict, total=False):
    colors: Required[BrandColors]

    icons: Required[Icons]

    widget_background: Required[Annotated[WidgetBackground, PropertyInfo(alias="widgetBackground")]]

    border_radius: Annotated[Optional[str], PropertyInfo(alias="borderRadius")]

    disable_message_icon: Annotated[Optional[bool], PropertyInfo(alias="disableMessageIcon")]

    font_family: Annotated[Optional[str], PropertyInfo(alias="fontFamily")]

    placement: Optional[Literal["top", "bottom", "left", "right"]]
