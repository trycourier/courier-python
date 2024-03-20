# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .utm import Utm

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MessageMetadata(pydantic.BaseModel):
    event: typing.Optional[str] = pydantic.Field(default=None)
    """
    An arbitrary string to tracks the event that generated this request (e.g. 'signup').
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of up to 9 tags you wish to associate with this request (and corresponding messages) for later analysis. Individual tags cannot be more than 30 characters in length.
    """

    utm: typing.Optional[Utm] = pydantic.Field(default=None)
    """
    Identify the campaign that refers traffic to a specific website, and attributes the browser's website session.
    """

    trace_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID used to correlate this request to processing on your servers. Note: Courier does not verify the uniqueness of this ID.
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
