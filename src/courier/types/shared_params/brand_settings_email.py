# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .email_head import EmailHead
from .email_footer import EmailFooter
from .email_header import EmailHeader
from .brand_template import BrandTemplate

__all__ = ["BrandSettingsEmail", "TemplateOverride"]


class TemplateOverride(BrandTemplate, total=False):
    mjml: Required[BrandTemplate]

    footer_background_color: Annotated[Optional[str], PropertyInfo(alias="footerBackgroundColor")]

    footer_full_width: Annotated[Optional[bool], PropertyInfo(alias="footerFullWidth")]


class BrandSettingsEmail(TypedDict, total=False):
    footer: Optional[EmailFooter]

    head: Optional[EmailHead]

    header: Optional[EmailHeader]

    template_override: Annotated[Optional[TemplateOverride], PropertyInfo(alias="templateOverride")]
