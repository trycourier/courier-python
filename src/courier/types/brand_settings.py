# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .brand_template import BrandTemplate

__all__ = [
    "BrandSettings",
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


class Colors(BaseModel):
    primary: Optional[str] = None

    secondary: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...
    else:
        __pydantic_extra__: Dict[str, str]


class EmailFooter(BaseModel):
    content: Optional[str] = None

    inherit_default: Optional[bool] = FieldInfo(alias="inheritDefault", default=None)


class EmailHead(BaseModel):
    inherit_default: bool = FieldInfo(alias="inheritDefault")

    content: Optional[str] = None


class EmailHeaderLogo(BaseModel):
    href: Optional[str] = None

    image: Optional[str] = None


class EmailHeader(BaseModel):
    logo: EmailHeaderLogo

    bar_color: Optional[str] = FieldInfo(alias="barColor", default=None)

    inherit_default: Optional[bool] = FieldInfo(alias="inheritDefault", default=None)


class EmailTemplateOverride(BrandTemplate):
    mjml: BrandTemplate

    footer_background_color: Optional[str] = FieldInfo(alias="footerBackgroundColor", default=None)

    footer_full_width: Optional[bool] = FieldInfo(alias="footerFullWidth", default=None)


class Email(BaseModel):
    footer: Optional[EmailFooter] = None

    head: Optional[EmailHead] = None

    header: Optional[EmailHeader] = None

    template_override: Optional[EmailTemplateOverride] = FieldInfo(alias="templateOverride", default=None)


class InappColors(BaseModel):
    primary: Optional[str] = None

    secondary: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...
    else:
        __pydantic_extra__: Dict[str, str]


class InappIcons(BaseModel):
    bell: Optional[str] = None

    message: Optional[str] = None


class InappWidgetBackground(BaseModel):
    bottom_color: Optional[str] = FieldInfo(alias="bottomColor", default=None)

    top_color: Optional[str] = FieldInfo(alias="topColor", default=None)


class Inapp(BaseModel):
    colors: InappColors

    icons: InappIcons

    widget_background: InappWidgetBackground = FieldInfo(alias="widgetBackground")

    border_radius: Optional[str] = FieldInfo(alias="borderRadius", default=None)

    disable_message_icon: Optional[bool] = FieldInfo(alias="disableMessageIcon", default=None)

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)

    placement: Optional[Literal["top", "bottom", "left", "right"]] = None


class BrandSettings(BaseModel):
    colors: Optional[Colors] = None

    email: Optional[Email] = None

    inapp: Optional[Inapp] = None
