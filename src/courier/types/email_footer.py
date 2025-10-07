# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailFooter"]


class EmailFooter(BaseModel):
    content: Optional[str] = None

    inherit_default: Optional[bool] = FieldInfo(alias="inheritDefault", default=None)
