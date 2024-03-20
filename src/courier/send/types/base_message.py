# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .delay import Delay
from .expiry import Expiry
from .message_channels import MessageChannels
from .message_context import MessageContext
from .message_data import MessageData
from .message_metadata import MessageMetadata
from .message_providers import MessageProviders
from .routing import Routing
from .timeout import Timeout

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BaseMessage(pydantic.BaseModel):
    data: typing.Optional[MessageData] = pydantic.Field(default=None)
    """
    An arbitrary object that includes any data you want to pass to the message.
    The data will populate the corresponding template or elements variables.
    """

    brand_id: typing.Optional[str] = None
    channels: typing.Optional[MessageChannels] = pydantic.Field(default=None)
    """
    "Define run-time configuration for one or more channels. If you don't specify channels, the default configuration for each channel will be used. Valid ChannelId's are: email, sms, push, inbox, direct_message, banner, and webhook."
    """

    context: typing.Optional[MessageContext] = pydantic.Field(default=None)
    """
    Context to load with this recipient. Will override any context set on message.context.
    """

    metadata: typing.Optional[MessageMetadata] = pydantic.Field(default=None)
    """
    Metadata such as utm tracking attached with the notification through this channel.
    """

    providers: typing.Optional[MessageProviders] = pydantic.Field(default=None)
    """
    An object whose keys are valid provider identifiers which map to an object.
    """

    routing: typing.Optional[Routing] = None
    timeout: typing.Optional[Timeout] = pydantic.Field(default=None)
    """
    Time in ms to attempt the channel before failing over to the next available channel.
    """

    delay: typing.Optional[Delay] = pydantic.Field(default=None)
    """
    Defines the time to wait before delivering the message.
    """

    expiry: typing.Optional[Expiry] = pydantic.Field(default=None)
    """
    "Expiry allows you to set an absolute or relative time in which a message expires.
    Note: This is only valid for the Courier Inbox channel as of 12-08-2022."
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
