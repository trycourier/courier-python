# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["MessageRoutingParam"]


class MessageRoutingParam(TypedDict, total=False):
    channels: Required[SequenceNotStr["MessageRoutingChannelParam"]]

    method: Required[Literal["all", "single"]]


from .message_routing_channel_param import MessageRoutingChannelParam
