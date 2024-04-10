# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .routing_channel import RoutingChannel
from .routing_method import RoutingMethod


class Routing(pydantic_v1.BaseModel):
    """
    Allows you to customize which channel(s) Courier will potentially deliver the message.
    If no routing key is specified, Courier will use the default routing configuration or
    routing defined by the template.
    """

    method: RoutingMethod
    channels: typing.List[RoutingChannel] = pydantic_v1.Field()
    """
    A list of channels or providers to send the message through. Can also recursively define
    sub-routing methods, which can be useful for defining advanced push notification
    delivery strategies.
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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
