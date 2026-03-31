# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .utm import Utm

__all__ = ["ChannelMetadata"]


class ChannelMetadata(TypedDict, total=False):
    utm: Optional[Utm]
