# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChannelClassification(str, enum.Enum):
    DIRECT_MESSAGE = "direct_message"
    EMAIL = "email"
    PUSH = "push"
    SMS = "sms"
    WEBHOOK = "webhook"
    INBOX = "inbox"

    def visit(
        self,
        direct_message: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        push: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
        webhook: typing.Callable[[], T_Result],
        inbox: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelClassification.DIRECT_MESSAGE:
            return direct_message()
        if self is ChannelClassification.EMAIL:
            return email()
        if self is ChannelClassification.PUSH:
            return push()
        if self is ChannelClassification.SMS:
            return sms()
        if self is ChannelClassification.WEBHOOK:
            return webhook()
        if self is ChannelClassification.INBOX:
            return inbox()
