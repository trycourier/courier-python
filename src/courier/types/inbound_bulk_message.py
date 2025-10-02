# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional

from .._models import BaseModel
from .base_message import BaseMessage

__all__ = ["InboundBulkMessage", "MessageInboundBulkTemplateMessage", "MessageInboundBulkContentMessage"]


class MessageInboundBulkTemplateMessage(BaseMessage):
    template: str
    """The id of the notification template to be rendered and sent to the recipient(s).

    This field or the content field must be supplied.
    """


class MessageInboundBulkContentMessage(BaseMessage):
    content: "Content"
    """
    Describes the content of the message in a way that will work for email, push,
    chat, or any channel. Either this or template must be specified.
    """


class InboundBulkMessage(BaseModel):
    brand: Optional[str] = None
    """
    A unique identifier that represents the brand that should be used for rendering
    the notification.
    """

    data: Optional[Dict[str, object]] = None
    """JSON that includes any data you want to pass to a message template.

    The data will populate the corresponding template variables.
    """

    event: Optional[str] = None

    locale: Optional[Dict[str, object]] = None

    message: Union[MessageInboundBulkTemplateMessage, MessageInboundBulkContentMessage, None] = None
    """
    Describes the content of the message in a way that will work for email, push,
    chat, or any channel.
    """

    override: Optional[object] = None
    """
    JSON that is merged into the request sent by Courier to the provider to override
    properties or to gain access to features in the provider API that are not
    natively supported by Courier.
    """


from .content import Content
