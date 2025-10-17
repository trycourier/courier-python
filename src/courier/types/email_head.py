# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailHead"]


class EmailHead(BaseModel):
    inherit_default: bool = FieldInfo(alias="inheritDefault")

    content: Optional[str] = None
