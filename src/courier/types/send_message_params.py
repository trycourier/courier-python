# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.utm import Utm
from .shared_params.recipient import Recipient
from .shared_params.user_recipient import UserRecipient
from .shared_params.message_context import MessageContext
from .shared_params.elemental_content import ElementalContent
from .shared_params.elemental_content_sugar import ElementalContentSugar

__all__ = [
    "SendMessageParams",
    "Message",
    "MessageChannels",
    "MessageChannelsMetadata",
    "MessageChannelsTimeouts",
    "MessageContent",
    "MessageDelay",
    "MessageExpiry",
    "MessageMetadata",
    "MessagePreferences",
    "MessageProviders",
    "MessageProvidersMetadata",
    "MessageRouting",
    "MessageTimeout",
    "MessageTo",
]


class SendMessageParams(TypedDict, total=False):
    message: Required[Message]
    """The message property has the following primary top-level properties.

    They define the destination and content of the message.
    """


class MessageChannelsMetadata(TypedDict, total=False):
    utm: Optional[Utm]


class MessageChannelsTimeouts(TypedDict, total=False):
    channel: Optional[int]

    provider: Optional[int]


_MessageChannelsReservedKeywords = TypedDict(
    "_MessageChannelsReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class MessageChannels(_MessageChannelsReservedKeywords, total=False):
    brand_id: Optional[str]
    """Brand id used for rendering."""

    metadata: Optional[MessageChannelsMetadata]

    override: Optional[Dict[str, object]]
    """Channel specific overrides."""

    providers: Optional[SequenceNotStr[str]]
    """Providers enabled for this channel."""

    routing_method: Optional[Literal["all", "single"]]
    """Defaults to `single`."""

    timeouts: Optional[MessageChannelsTimeouts]


MessageContent: TypeAlias = Union[ElementalContentSugar, ElementalContent]


class MessageDelay(TypedDict, total=False):
    duration: Optional[int]
    """The duration of the delay in milliseconds."""

    until: Optional[str]
    """ISO 8601 timestamp or opening_hours-like format."""


class MessageExpiry(TypedDict, total=False):
    expires_in: Required[Union[str, int]]
    """Duration in ms or ISO8601 duration (e.g. P1DT4H)."""

    expires_at: Optional[str]
    """Epoch or ISO8601 timestamp with timezone."""


class MessageMetadata(TypedDict, total=False):
    event: Optional[str]

    tags: Optional[SequenceNotStr[str]]

    trace_id: Optional[str]

    utm: Optional[Utm]


class MessagePreferences(TypedDict, total=False):
    subscription_topic_id: Required[str]
    """The subscription topic to apply to the message."""


class MessageProvidersMetadata(TypedDict, total=False):
    utm: Optional[Utm]


_MessageProvidersReservedKeywords = TypedDict(
    "_MessageProvidersReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class MessageProviders(_MessageProvidersReservedKeywords, total=False):
    metadata: Optional[MessageProvidersMetadata]

    override: Optional[Dict[str, object]]
    """Provider-specific overrides."""

    timeouts: Optional[int]


class MessageRouting(TypedDict, total=False):
    channels: Required[SequenceNotStr["MessageRoutingChannel"]]
    """A list of channels or providers (or nested routing rules)."""

    method: Required[Literal["all", "single"]]


class MessageTimeout(TypedDict, total=False):
    channel: Optional[Dict[str, int]]

    criteria: Optional[Literal["no-escalation", "delivered", "viewed", "engaged"]]

    escalation: Optional[int]

    message: Optional[int]

    provider: Optional[Dict[str, int]]


MessageTo: TypeAlias = Union[UserRecipient, Iterable[Recipient]]


class Message(TypedDict, total=False):
    brand_id: Optional[str]

    channels: Optional[Dict[str, MessageChannels]]
    """Define run-time configuration for channels.

    Valid ChannelId's: email, sms, push, inbox, direct_message, banner, webhook.
    """

    content: MessageContent
    """
    Describes content that will work for email, inbox, push, chat, or any channel
    id.
    """

    context: Optional[MessageContext]

    data: Optional[Dict[str, object]]

    delay: Optional[MessageDelay]

    expiry: Optional[MessageExpiry]

    metadata: Optional[MessageMetadata]

    preferences: Optional[MessagePreferences]

    providers: Optional[Dict[str, MessageProviders]]

    routing: Optional[MessageRouting]
    """Customize which channels/providers Courier may deliver the message through."""

    template: Optional[str]

    timeout: Optional[MessageTimeout]

    to: Optional[MessageTo]
    """The recipient or a list of recipients of the message"""


from .shared_params.message_routing_channel import MessageRoutingChannel
