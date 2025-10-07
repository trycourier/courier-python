# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageRouting"]


class MessageRouting(BaseModel):
    channels: List["MessageRoutingChannel"]

    method: Literal["all", "single"]


from .message_routing_channel import MessageRoutingChannel
