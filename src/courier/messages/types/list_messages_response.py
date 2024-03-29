# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...commons.types.paging import Paging
from ...core.datetime_utils import serialize_datetime
from .message_details import MessageDetails

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ListMessagesResponse(pydantic.BaseModel):
    paging: Paging = pydantic.Field()
    """
    Paging information for the result set.
    """

    results: typing.List[MessageDetails] = pydantic.Field()
    """
    An array of messages with their details.
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
