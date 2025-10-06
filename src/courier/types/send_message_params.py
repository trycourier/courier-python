# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .utm_param import UtmParam
from .recipient_param import RecipientParam
from .preference_param import PreferenceParam
from .elemental_node_param import ElementalNodeParam
from .message_context_param import MessageContextParam

__all__ = [
    "SendMessageParams",
    "Message",
    "MessageContent",
    "MessageContentElementalContentSugar",
    "MessageContentElementalContent",
    "MessageChannels",
    "MessageChannelsMetadata",
    "MessageChannelsTimeouts",
    "MessageDelay",
    "MessageExpiry",
    "MessageMetadata",
    "MessagePreferences",
    "MessageProviders",
    "MessageProvidersMetadata",
    "MessageRouting",
    "MessageTimeout",
    "MessageTo",
    "MessageToUnionMember0",
    "MessageToUnionMember0Preferences",
]


class SendMessageParams(TypedDict, total=False):
    message: Required[Message]
    """The message property has the following primary top-level properties.

    They define the destination and content of the message.
    """


class MessageContentElementalContentSugar(TypedDict, total=False):
    body: Required[str]
    """The text content displayed in the notification."""

    title: Required[str]
    """Title/subject displayed by supported channels."""


class MessageContentElementalContent(TypedDict, total=False):
    elements: Required[Iterable[ElementalNodeParam]]

    version: Required[str]
    """For example, "2022-01-01" """

    brand: object


MessageContent: TypeAlias = Union[MessageContentElementalContentSugar, MessageContentElementalContent]


class MessageChannelsMetadata(TypedDict, total=False):
    utm: Optional[UtmParam]


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

    utm: Optional[UtmParam]


class MessagePreferences(TypedDict, total=False):
    subscription_topic_id: Required[str]
    """The subscription topic to apply to the message."""


class MessageProvidersMetadata(TypedDict, total=False):
    utm: Optional[UtmParam]


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
    channels: Required[SequenceNotStr["MessageRoutingChannelParam"]]
    """A list of channels or providers (or nested routing rules)."""

    method: Required[Literal["all", "single"]]


class MessageTimeout(TypedDict, total=False):
    channel: Optional[Dict[str, int]]

    criteria: Optional[Literal["no-escalation", "delivered", "viewed", "engaged"]]

    escalation: Optional[int]

    message: Optional[int]

    provider: Optional[Dict[str, int]]


class MessageToUnionMember0Preferences(TypedDict, total=False):
    notifications: Required[Dict[str, PreferenceParam]]

    categories: Optional[Dict[str, PreferenceParam]]

    template_id: Annotated[Optional[str], PropertyInfo(alias="templateId")]


class MessageToUnionMember0(TypedDict, total=False):
    account_id: Optional[str]
    """Use `tenant_id` instead."""

    context: Optional[MessageContextParam]
    """Context such as tenant_id to send the notification with."""

    data: Optional[Dict[str, object]]

    email: Optional[str]

    locale: Optional[str]
    """The user's preferred ISO 639-1 language code."""

    phone_number: Optional[str]

    preferences: Optional[MessageToUnionMember0Preferences]

    tenant_id: Optional[str]
    """Tenant id. Will load brand, default preferences and base context data."""

    user_id: Optional[str]


MessageTo: TypeAlias = Union[MessageToUnionMember0, Iterable[RecipientParam]]


class Message(TypedDict, total=False):
    content: Required[MessageContent]
    """
    Describes content that will work for email, inbox, push, chat, or any channel
    id.
    """

    brand_id: Optional[str]

    channels: Optional[Dict[str, MessageChannels]]
    """Define run-time configuration for channels.

    Valid ChannelId's: email, sms, push, inbox, direct_message, banner, webhook.
    """

    context: Optional[MessageContextParam]

    data: Optional[Dict[str, object]]

    delay: Optional[MessageDelay]

    expiry: Optional[MessageExpiry]

    metadata: Optional[MessageMetadata]

    preferences: Optional[MessagePreferences]

    providers: Optional[Dict[str, MessageProviders]]

    routing: Optional[MessageRouting]
    """Customize which channels/providers Courier may deliver the message through."""

    timeout: Optional[MessageTimeout]

    to: Optional[MessageTo]
    """The recipient or a list of recipients of the message"""


from .message_routing_channel_param import MessageRoutingChannelParam
