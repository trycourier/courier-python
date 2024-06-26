# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ...core.unchecked_base_model import UncheckedBaseModel
from .message_status import MessageStatus
from .reason import Reason


class MessageDetails(UncheckedBaseModel):
    id: str = pydantic_v1.Field()
    """
    A unique identifier associated with the message you wish to retrieve (results from a send).
    """

    status: MessageStatus = pydantic_v1.Field()
    """
    The current status of the message.
    """

    enqueued: int = pydantic_v1.Field()
    """
    A UTC timestamp at which Courier received the message request. Stored as a millisecond representation of the Unix epoch.
    """

    sent: int = pydantic_v1.Field()
    """
    A UTC timestamp at which Courier passed the message to the Integration provider. Stored as a millisecond representation of the Unix epoch.
    """

    delivered: int = pydantic_v1.Field()
    """
    A UTC timestamp at which the Integration provider delivered the message. Stored as a millisecond representation of the Unix epoch.
    """

    opened: int = pydantic_v1.Field()
    """
    A UTC timestamp at which the recipient opened a message for the first time. Stored as a millisecond representation of the Unix epoch.
    """

    clicked: int = pydantic_v1.Field()
    """
    A UTC timestamp at which the recipient clicked on a tracked link for the first time. Stored as a millisecond representation of the Unix epoch.
    """

    recipient: str = pydantic_v1.Field()
    """
    A unique identifier associated with the recipient of the delivered message.
    """

    event: str = pydantic_v1.Field()
    """
    A unique identifier associated with the event of the delivered message.
    """

    notification: str = pydantic_v1.Field()
    """
    A unique identifier associated with the notification of the delivered message.
    """

    error: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    A message describing the error that occurred.
    """

    reason: typing.Optional[Reason] = pydantic_v1.Field(default=None)
    """
    The reason for the current status of the message.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
