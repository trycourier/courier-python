# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChannelSource(str, enum.Enum):
    SUBSCRIPTION = "subscription"
    LIST = "list"
    RECIPIENT = "recipient"

    def visit(
        self,
        subscription: typing.Callable[[], T_Result],
        list: typing.Callable[[], T_Result],
        recipient: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelSource.SUBSCRIPTION:
            return subscription()
        if self is ChannelSource.LIST:
            return list()
        if self is ChannelSource.RECIPIENT:
            return recipient()
