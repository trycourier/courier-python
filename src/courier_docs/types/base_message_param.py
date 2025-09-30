# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .utm_param import UtmParam
from .routing_method import RoutingMethod
from .message_context_param import MessageContextParam

__all__ = [
    "BaseMessageParam",
    "Channels",
    "ChannelsMetadata",
    "ChannelsTimeouts",
    "Delay",
    "Expiry",
    "Metadata",
    "Preferences",
    "Providers",
    "ProvidersMetadata",
    "Routing",
    "RoutingChannel",
    "RoutingChannelRoutingStrategyChannel",
    "RoutingChannelRoutingStrategyChannelProviders",
    "RoutingChannelRoutingStrategyChannelProvidersMetadata",
    "RoutingChannelRoutingStrategyProvider",
    "RoutingChannelRoutingStrategyProviderMetadata",
    "Timeout",
]


class ChannelsMetadata(TypedDict, total=False):
    utm: Optional[UtmParam]


class ChannelsTimeouts(TypedDict, total=False):
    channel: Optional[int]

    provider: Optional[int]


_ChannelsReservedKeywords = TypedDict(
    "_ChannelsReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class Channels(_ChannelsReservedKeywords, total=False):
    brand_id: Optional[str]
    """Id of the brand that should be used for rendering the message.

    If not specified, the brand configured as default brand will be used.
    """

    metadata: Optional[ChannelsMetadata]

    override: Optional[Dict[str, object]]
    """Channel specific overrides."""

    providers: Optional[SequenceNotStr[str]]
    """A list of providers enabled for this channel.

    Courier will select one provider to send through unless routing_method is set to
    all.
    """

    routing_method: Optional[RoutingMethod]
    """The method for selecting the providers to send the message with.

    Single will send to one of the available providers for this channel, all will
    send the message through all channels. Defaults to `single`.
    """

    timeouts: Optional[ChannelsTimeouts]


class Delay(TypedDict, total=False):
    duration: Optional[int]
    """The duration of the delay in milliseconds."""

    until: Optional[str]
    """
    An ISO 8601 timestamp that specifies when it should be delivered or an
    OpenStreetMap opening_hours-like format that specifies the
    [Delivery Window](https://www.courier.com/docs/platform/sending/failover/#delivery-window)
    (e.g., 'Mo-Fr 08:00-18:00pm')
    """


class Expiry(TypedDict, total=False):
    expires_in: Required[Union[str, int]]
    """A duration in the form of milliseconds or an ISO8601 Duration format (i.e.

    P1DT4H).
    """

    expires_at: Optional[str]
    """
    An epoch timestamp or ISO8601 timestamp with timezone
    `(YYYY-MM-DDThh:mm:ss.sTZD)` that describes the time in which a message expires.
    """


class Metadata(TypedDict, total=False):
    event: Optional[str]
    """An arbitrary string to tracks the event that generated this request (e.g.

    'signup').
    """

    tags: Optional[SequenceNotStr[str]]
    """
    An array of up to 9 tags you wish to associate with this request (and
    corresponding messages) for later analysis. Individual tags cannot be more than
    30 characters in length.
    """

    trace_id: Optional[str]
    """A unique ID used to correlate this request to processing on your servers.

    Note: Courier does not verify the uniqueness of this ID.
    """

    utm: Optional[UtmParam]
    """
    Identify the campaign that refers traffic to a specific website, and attributes
    the browser's website session.
    """


class Preferences(TypedDict, total=False):
    subscription_topic_id: Required[str]
    """The ID of the subscription topic you want to apply to the message.

    If this is a templated message, it will override the subscription topic if
    already associated
    """


class ProvidersMetadata(TypedDict, total=False):
    utm: Optional[UtmParam]


_ProvidersReservedKeywords = TypedDict(
    "_ProvidersReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class Providers(_ProvidersReservedKeywords, total=False):
    metadata: Optional[ProvidersMetadata]

    override: Optional[Dict[str, object]]
    """Provider specific overrides."""

    timeouts: Optional[int]


class RoutingChannelRoutingStrategyChannelProvidersMetadata(TypedDict, total=False):
    utm: Optional[UtmParam]


_RoutingChannelRoutingStrategyChannelProvidersReservedKeywords = TypedDict(
    "_RoutingChannelRoutingStrategyChannelProvidersReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class RoutingChannelRoutingStrategyChannelProviders(
    _RoutingChannelRoutingStrategyChannelProvidersReservedKeywords, total=False
):
    metadata: Optional[RoutingChannelRoutingStrategyChannelProvidersMetadata]

    override: Optional[Dict[str, object]]
    """Provider specific overrides."""

    timeouts: Optional[int]


_RoutingChannelRoutingStrategyChannelReservedKeywords = TypedDict(
    "_RoutingChannelRoutingStrategyChannelReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class RoutingChannelRoutingStrategyChannel(_RoutingChannelRoutingStrategyChannelReservedKeywords, total=False):
    channel: Required[str]

    config: Optional[Dict[str, object]]

    method: Optional[RoutingMethod]

    providers: Optional[Dict[str, RoutingChannelRoutingStrategyChannelProviders]]


class RoutingChannelRoutingStrategyProviderMetadata(TypedDict, total=False):
    utm: Optional[UtmParam]


_RoutingChannelRoutingStrategyProviderReservedKeywords = TypedDict(
    "_RoutingChannelRoutingStrategyProviderReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class RoutingChannelRoutingStrategyProvider(_RoutingChannelRoutingStrategyProviderReservedKeywords, total=False):
    metadata: Required[RoutingChannelRoutingStrategyProviderMetadata]

    name: Required[str]

    config: Optional[Dict[str, object]]


RoutingChannel: TypeAlias = Union[RoutingChannelRoutingStrategyChannel, RoutingChannelRoutingStrategyProvider, str]


class Routing(TypedDict, total=False):
    channels: Required[SequenceNotStr[RoutingChannel]]
    """A list of channels or providers to send the message through.

    Can also recursively define sub-routing methods, which can be useful for
    defining advanced push notification delivery strategies.
    """

    method: Required[RoutingMethod]


class Timeout(TypedDict, total=False):
    channel: Optional[Dict[str, int]]

    criteria: Optional[Literal["no-escalation", "delivered", "viewed", "engaged"]]

    escalation: Optional[int]

    message: Optional[int]

    provider: Optional[Dict[str, int]]


class BaseMessageParam(TypedDict, total=False):
    brand_id: Optional[str]

    channels: Optional[Dict[str, Channels]]
    """\"Define run-time configuration for one or more channels.

    If you don't specify channels, the default configuration for each channel will
    be used. Valid ChannelId's are: email, sms, push, inbox, direct_message, banner,
    and webhook."
    """

    context: Optional[MessageContextParam]
    """Context to load with this recipient.

    Will override any context set on message.context.
    """

    data: Optional[Dict[str, object]]
    """
    An arbitrary object that includes any data you want to pass to the message. The
    data will populate the corresponding template or elements variables.
    """

    delay: Optional[Delay]
    """Defines the time to wait before delivering the message.

    You can specify one of the following options. Duration with the number of
    milliseconds to delay. Until with an ISO 8601 timestamp that specifies when it
    should be delivered. Until with an OpenStreetMap opening_hours-like format that
    specifies the
    [Delivery Window](https://www.courier.com/docs/platform/sending/failover/#delivery-window)
    (e.g., 'Mo-Fr 08:00-18:00pm')
    """

    expiry: Optional[Expiry]
    """
    "Expiry allows you to set an absolute or relative time in which a message
    expires. Note: This is only valid for the Courier Inbox channel as of
    12-08-2022."
    """

    metadata: Optional[Metadata]
    """
    Metadata such as utm tracking attached with the notification through this
    channel.
    """

    preferences: Optional[Preferences]

    providers: Optional[Dict[str, Providers]]
    """An object whose keys are valid provider identifiers which map to an object."""

    routing: Optional[Routing]
    """
    Allows you to customize which channel(s) Courier will potentially deliver the
    message. If no routing key is specified, Courier will use the default routing
    configuration or routing defined by the template.
    """

    timeout: Optional[Timeout]
    """
    Time in ms to attempt the channel before failing over to the next available
    channel.
    """
