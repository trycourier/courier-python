# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .brand_template_param import BrandTemplateParam

__all__ = [
    "BrandSettingsParam",
    "Colors",
    "Email",
    "EmailFooter",
    "EmailHead",
    "EmailHeader",
    "EmailHeaderLogo",
    "EmailTemplateOverride",
    "Inapp",
    "InappColors",
    "InappIcons",
    "InappWidgetBackground",
]


class ColorsTyped(TypedDict, total=False):
    primary: Optional[str]

    secondary: Optional[str]


Colors: TypeAlias = Union[ColorsTyped, Dict[str, str]]


class EmailFooter(TypedDict, total=False):
    content: Optional[str]

    inherit_default: Annotated[Optional[bool], PropertyInfo(alias="inheritDefault")]


class EmailHead(TypedDict, total=False):
    inherit_default: Required[Annotated[bool, PropertyInfo(alias="inheritDefault")]]

    content: Optional[str]


class EmailHeaderLogo(TypedDict, total=False):
    href: Optional[str]

    image: Optional[str]


class EmailHeader(TypedDict, total=False):
    logo: Required[EmailHeaderLogo]

    bar_color: Annotated[Optional[str], PropertyInfo(alias="barColor")]

    inherit_default: Annotated[Optional[bool], PropertyInfo(alias="inheritDefault")]


class EmailTemplateOverride(BrandTemplateParam, total=False):
    mjml: Required[BrandTemplateParam]

    footer_background_color: Annotated[Optional[str], PropertyInfo(alias="footerBackgroundColor")]

    footer_full_width: Annotated[Optional[bool], PropertyInfo(alias="footerFullWidth")]


class Email(TypedDict, total=False):
    footer: Optional[EmailFooter]

    head: Optional[EmailHead]

    header: Optional[EmailHeader]

    template_override: Annotated[Optional[EmailTemplateOverride], PropertyInfo(alias="templateOverride")]


class InappColorsTyped(TypedDict, total=False):
    primary: Optional[str]

    secondary: Optional[str]


InappColors: TypeAlias = Union[InappColorsTyped, Dict[str, str]]


class InappIcons(TypedDict, total=False):
    bell: Optional[str]

    message: Optional[str]


class InappWidgetBackground(TypedDict, total=False):
    bottom_color: Annotated[Optional[str], PropertyInfo(alias="bottomColor")]

    top_color: Annotated[Optional[str], PropertyInfo(alias="topColor")]


class Inapp(TypedDict, total=False):
    colors: Required[InappColors]

    icons: Required[InappIcons]

    widget_background: Required[Annotated[InappWidgetBackground, PropertyInfo(alias="widgetBackground")]]

    border_radius: Annotated[Optional[str], PropertyInfo(alias="borderRadius")]

    disable_message_icon: Annotated[Optional[bool], PropertyInfo(alias="disableMessageIcon")]

    font_family: Annotated[Optional[str], PropertyInfo(alias="fontFamily")]

    placement: Optional[Literal["top", "bottom", "left", "right"]]


class BrandSettingsParam(TypedDict, total=False):
    colors: Optional[Colors]

    email: Optional[Email]

    inapp: Optional[Inapp]
