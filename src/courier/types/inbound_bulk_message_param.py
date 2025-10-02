# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

from .content_param import ContentParam
from .base_message_param import BaseMessageParam

__all__ = ["InboundBulkMessageParam", "MessageInboundBulkTemplateMessage", "MessageInboundBulkContentMessage"]


class MessageInboundBulkTemplateMessage(BaseMessageParam, total=False):
    template: Required[str]
    """The id of the notification template to be rendered and sent to the recipient(s).

    This field or the content field must be supplied.
    """


class MessageInboundBulkContentMessage(BaseMessageParam, total=False):
    content: Required[ContentParam]
    """
    Describes the content of the message in a way that will work for email, push,
    chat, or any channel. Either this or template must be specified.
    """


class InboundBulkMessageParam(TypedDict, total=False):
    brand: Optional[str]
    """
    A unique identifier that represents the brand that should be used for rendering
    the notification.
    """

    data: Optional[Dict[str, object]]
    """JSON that includes any data you want to pass to a message template.

    The data will populate the corresponding template variables.
    """

    event: Optional[str]

    locale: Optional[Dict[str, object]]

    message: Union[MessageInboundBulkTemplateMessage, MessageInboundBulkContentMessage, None]
    """
    Describes the content of the message in a way that will work for email, push,
    chat, or any channel.
    """

    override: object
    """
    JSON that is merged into the request sent by Courier to the provider to override
    properties or to gain access to features in the provider API that are not
    natively supported by Courier.
    """
