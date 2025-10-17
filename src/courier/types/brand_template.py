# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BrandTemplate"]


class BrandTemplate(BaseModel):
    enabled: bool

    background_color: Optional[str] = FieldInfo(alias="backgroundColor", default=None)

    blocks_background_color: Optional[str] = FieldInfo(alias="blocksBackgroundColor", default=None)

    footer: Optional[str] = None

    head: Optional[str] = None

    header: Optional[str] = None

    width: Optional[str] = None
