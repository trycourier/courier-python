# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .email_head import EmailHead
from .email_footer import EmailFooter
from .email_header import EmailHeader
from .brand_template import BrandTemplate

__all__ = ["BrandSettingsEmail", "TemplateOverride"]


class TemplateOverride(BrandTemplate):
    mjml: BrandTemplate

    footer_background_color: Optional[str] = FieldInfo(alias="footerBackgroundColor", default=None)

    footer_full_width: Optional[bool] = FieldInfo(alias="footerFullWidth", default=None)


class BrandSettingsEmail(BaseModel):
    footer: Optional[EmailFooter] = None

    head: Optional[EmailHead] = None

    header: Optional[EmailHeader] = None

    template_override: Optional[TemplateOverride] = FieldInfo(alias="templateOverride", default=None)
