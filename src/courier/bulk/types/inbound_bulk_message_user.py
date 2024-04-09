# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...commons.types.recipient_preferences import RecipientPreferences
from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...send.types.user_recipient import UserRecipient


class InboundBulkMessageUser(pydantic_v1.BaseModel):
    preferences: typing.Optional[RecipientPreferences] = None
    profile: typing.Optional[typing.Any] = None
    recipient: typing.Optional[str] = None
    data: typing.Optional[typing.Any] = None
    to: typing.Optional[UserRecipient] = None

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
