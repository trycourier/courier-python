# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .utm import Utm
from ..._models import BaseModel

__all__ = ["ChannelMetadata"]


class ChannelMetadata(BaseModel):
    utm: Optional[Utm] = None
