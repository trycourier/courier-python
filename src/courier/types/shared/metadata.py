# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .utm import Utm
from ..._models import BaseModel

__all__ = ["Metadata"]


class Metadata(BaseModel):
    utm: Optional[Utm] = None
