# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from .message_status import MessageStatus
from .reason import Reason

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MessageDetails(pydantic.BaseModel):
    id: str = pydantic.Field()
    """
    A unique identifier associated with the message you wish to retrieve (results from a send).
    """

    status: MessageStatus = pydantic.Field()
    """
    The current status of the message.
    """

    enqueued: int = pydantic.Field()
    """
    A UTC timestamp at which Courier received the message request. Stored as a millisecond representation of the Unix epoch.
    """

    sent: int = pydantic.Field()
    """
    A UTC timestamp at which Courier passed the message to the Integration provider. Stored as a millisecond representation of the Unix epoch.
    """

    delivered: int = pydantic.Field()
    """
    A UTC timestamp at which the Integration provider delivered the message. Stored as a millisecond representation of the Unix epoch.
    """

    opened: int = pydantic.Field()
    """
    A UTC timestamp at which the recipient opened a message for the first time. Stored as a millisecond representation of the Unix epoch.
    """

    clicked: int = pydantic.Field()
    """
    A UTC timestamp at which the recipient clicked on a tracked link for the first time. Stored as a millisecond representation of the Unix epoch.
    """

    recipient: str = pydantic.Field()
    """
    A unique identifier associated with the recipient of the delivered message.
    """

    event: str = pydantic.Field()
    """
    A unique identifier associated with the event of the delivered message.
    """

    notification: str = pydantic.Field()
    """
    A unique identifier associated with the notification of the delivered message.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    A message describing the error that occurred.
    """

    reason: typing.Optional[Reason] = pydantic.Field(default=None)
    """
    The reason for the current status of the message.
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
