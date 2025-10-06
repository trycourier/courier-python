# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    archived: Optional[bool]
    """
    A boolean value that indicates whether archived messages should be included in
    the response.
    """

    cursor: Optional[str]
    """A unique identifier that allows for fetching the next set of messages."""

    enqueued_after: Optional[str]
    """The enqueued datetime of a message to filter out messages received before."""

    event: Optional[str]
    """A unique identifier representing the event that was used to send the event."""

    list: Optional[str]
    """A unique identifier representing the list the message was sent to."""

    message_id: Annotated[Optional[str], PropertyInfo(alias="messageId")]
    """
    A unique identifier representing the message_id returned from either /send or
    /send/list.
    """

    notification: Optional[str]
    """
    A unique identifier representing the notification that was used to send the
    event.
    """

    provider: SequenceNotStr[Optional[str]]
    """The key assocated to the provider you want to filter on.

    E.g., sendgrid, inbox, twilio, slack, msteams, etc. Allows multiple values to be
    set in query parameters.
    """

    recipient: Optional[str]
    """
    A unique identifier representing the recipient associated with the requested
    profile.
    """

    status: SequenceNotStr[Optional[str]]
    """An indicator of the current status of the message.

    Allows multiple values to be set in query parameters.
    """

    tag: SequenceNotStr[Optional[str]]
    """A tag placed in the metadata.tags during a notification send.

    Allows multiple values to be set in query parameters.
    """

    tags: Optional[str]
    """A comma delimited list of 'tags'.

    Messages will be returned if they match any of the tags passed in.
    """

    tenant_id: Optional[str]
    """Messages sent with the context of a Tenant"""

    trace_id: Annotated[Optional[str], PropertyInfo(alias="traceId")]
    """The unique identifier used to trace the requests"""
