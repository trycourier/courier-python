# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Utm"]


class Utm(BaseModel):
    campaign: Optional[str] = None

    content: Optional[str] = None

    medium: Optional[str] = None

    source: Optional[str] = None

    term: Optional[str] = None
