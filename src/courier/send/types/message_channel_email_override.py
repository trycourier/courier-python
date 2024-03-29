# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...brands.types.brand import Brand
from ...core.datetime_utils import serialize_datetime
from .attachment import Attachment
from .tracking_override import TrackingOverride

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MessageChannelEmailOverride(pydantic.BaseModel):
    attachments: typing.Optional[typing.List[Attachment]] = None
    bcc: typing.Optional[str] = None
    brand: typing.Optional[Brand] = None
    cc: typing.Optional[str] = None
    from_: typing.Optional[str] = pydantic.Field(alias="from", default=None)
    html: typing.Optional[str] = None
    reply_to: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    text: typing.Optional[str] = None
    tracking: TrackingOverride

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
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
