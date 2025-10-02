# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1

__all__ = ["MessageRoutingChannelParam"]

if TYPE_CHECKING or not PYDANTIC_V1:
    MessageRoutingChannelParam = TypeAliasType("MessageRoutingChannelParam", Union[str, "MessageRoutingParam"])
else:
    MessageRoutingChannelParam: TypeAlias = Union[str, "MessageRoutingParam"]

from .message_routing_param import MessageRoutingParam
