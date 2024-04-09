# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .channel_metadata import ChannelMetadata
from .override import Override
from .routing_method import RoutingMethod
from .timeouts import Timeouts


class Channel(pydantic_v1.BaseModel):
    brand_id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Id of the brand that should be used for rendering the message.
    If not specified, the brand configured as default brand will be used.
    """

    providers: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    A list of providers enabled for this channel. Courier will select
    one provider to send through unless routing_method is set to all.
    """

    routing_method: typing.Optional[RoutingMethod] = pydantic_v1.Field(default=None)
    """
    The method for selecting the providers to send the message with.
    Single will send to one of the available providers for this channel,
    all will send the message through all channels. Defaults to `single`.
    """

    if_: typing.Optional[str] = pydantic_v1.Field(alias="if", default=None)
    """
    A JavaScript conditional expression to determine if the message should
    be sent through the channel. Has access to the data and profile object.
    For example, `data.name === profile.name`
    """

    timeouts: typing.Optional[Timeouts] = None
    override: typing.Optional[Override] = pydantic_v1.Field(default=None)
    """
    Channel specific overrides.
    """

    metadata: typing.Optional[ChannelMetadata] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}