# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .send_to_channel import SendToChannel
from .send_direct_message import SendDirectMessage

__all__ = ["Discord"]

Discord: TypeAlias = Union[SendToChannel, SendDirectMessage]
