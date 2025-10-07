# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .email_head_param import EmailHeadParam
from .email_footer_param import EmailFooterParam
from .email_header_param import EmailHeaderParam
from .brand_template_param import BrandTemplateParam

__all__ = ["BrandSettingsEmailParam", "TemplateOverride"]


class TemplateOverride(BrandTemplateParam, total=False):
    mjml: Required[BrandTemplateParam]

    footer_background_color: Annotated[Optional[str], PropertyInfo(alias="footerBackgroundColor")]

    footer_full_width: Annotated[Optional[bool], PropertyInfo(alias="footerFullWidth")]


class BrandSettingsEmailParam(TypedDict, total=False):
    footer: Optional[EmailFooterParam]

    head: Optional[EmailHeadParam]

    header: Optional[EmailHeaderParam]

    template_override: Annotated[Optional[TemplateOverride], PropertyInfo(alias="templateOverride")]
