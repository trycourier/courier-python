# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .timeouts import Timeouts
from ..._models import BaseModel
from .channel_metadata import ChannelMetadata

__all__ = ["Channel"]


class Channel(BaseModel):
    brand_id: Optional[str] = None
    """Brand id used for rendering."""

    if_: Optional[str] = FieldInfo(alias="if", default=None)
    """JS conditional with access to data/profile."""

    metadata: Optional[ChannelMetadata] = None

    override: Optional[Dict[str, object]] = None
    """Channel specific overrides."""

    providers: Optional[List[str]] = None
    """Providers enabled for this channel."""

    routing_method: Optional[Literal["all", "single"]] = None
    """Defaults to `single`."""

    timeouts: Optional[Timeouts] = None
