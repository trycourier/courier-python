# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias

from .content_param import ContentParam
from .base_message_param import BaseMessageParam
from .base_message_send_to_param import BaseMessageSendToParam

__all__ = ["MessageParam", "ContentMessage", "TemplateMessage"]


class ContentMessage(BaseMessageParam, BaseMessageSendToParam, total=False):
    content: Required[ContentParam]
    """
    Describes the content of the message in a way that will work for email, push,
    chat, or any channel. Either this or template must be specified.
    """


class TemplateMessage(BaseMessageParam, BaseMessageSendToParam, total=False):
    template: Required[str]
    """The id of the notification template to be rendered and sent to the recipient(s).

    This field or the content field must be supplied.
    """


MessageParam: TypeAlias = Union[ContentMessage, TemplateMessage]
