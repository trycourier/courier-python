# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .icons_param import IconsParam
from .brand_colors_param import BrandColorsParam
from .widget_background_param import WidgetBackgroundParam

__all__ = ["BrandSettingsInAppParam"]


class BrandSettingsInAppParam(TypedDict, total=False):
    colors: Required[BrandColorsParam]

    icons: Required[IconsParam]

    widget_background: Required[Annotated[WidgetBackgroundParam, PropertyInfo(alias="widgetBackground")]]

    border_radius: Annotated[Optional[str], PropertyInfo(alias="borderRadius")]

    disable_message_icon: Annotated[Optional[bool], PropertyInfo(alias="disableMessageIcon")]

    font_family: Annotated[Optional[str], PropertyInfo(alias="fontFamily")]

    placement: Optional[Literal["top", "bottom", "left", "right"]]
