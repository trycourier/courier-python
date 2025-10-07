# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from ..._compat import PYDANTIC_V1

__all__ = ["MessageRoutingChannel"]

if TYPE_CHECKING or not PYDANTIC_V1:
    MessageRoutingChannel = TypeAliasType("MessageRoutingChannel", Union[str, "MessageRouting"])
else:
    MessageRoutingChannel: TypeAlias = Union[str, "MessageRouting"]

from .message_routing import MessageRouting
