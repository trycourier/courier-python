# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .utm import Utm
from .._models import BaseModel
from .message_context import MessageContext

__all__ = [
    "BaseMessage",
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
    "Timeout",
]


class ChannelsMetadata(BaseModel):
    utm: Optional[Utm] = None


class ChannelsTimeouts(BaseModel):
    channel: Optional[int] = None

    provider: Optional[int] = None


class Channels(BaseModel):
    brand_id: Optional[str] = None
    """Id of the brand that should be used for rendering the message.

    If not specified, the brand configured as default brand will be used.
    """

    if_: Optional[str] = FieldInfo(alias="if", default=None)
    """
    A JavaScript conditional expression to determine if the message should be sent
    through the channel. Has access to the data and profile object. Only applies
    when a custom routing strategy is defined. For example,
    `data.name === profile.name`.
    """

    metadata: Optional[ChannelsMetadata] = None

    override: Optional[Dict[str, object]] = None
    """Channel specific overrides."""

    providers: Optional[List[str]] = None
    """A list of providers enabled for this channel.

    Courier will select one provider to send through unless routing_method is set to
    all.
    """

    routing_method: Optional[Literal["all", "single"]] = None
    """The method for selecting the providers to send the message with.

    Single will send to one of the available providers for this channel, all will
    send the message through all channels. Defaults to `single`.
    """

    timeouts: Optional[ChannelsTimeouts] = None


class Delay(BaseModel):
    duration: Optional[int] = None
    """The duration of the delay in milliseconds."""

    until: Optional[str] = None
    """
    An ISO 8601 timestamp that specifies when it should be delivered or an
    OpenStreetMap opening_hours-like format that specifies the
    [Delivery Window](https://www.courier.com/docs/platform/sending/failover/#delivery-window)
    (e.g., 'Mo-Fr 08:00-18:00pm')
    """


class Expiry(BaseModel):
    expires_in: Union[str, int]
    """A duration in the form of milliseconds or an ISO8601 Duration format (i.e.

    P1DT4H).
    """

    expires_at: Optional[str] = None
    """
    An epoch timestamp or ISO8601 timestamp with timezone
    `(YYYY-MM-DDThh:mm:ss.sTZD)` that describes the time in which a message expires.
    """


class Metadata(BaseModel):
    event: Optional[str] = None
    """An arbitrary string to tracks the event that generated this request (e.g.

    'signup').
    """

    tags: Optional[List[str]] = None
    """
    An array of up to 9 tags you wish to associate with this request (and
    corresponding messages) for later analysis. Individual tags cannot be more than
    30 characters in length.
    """

    trace_id: Optional[str] = None
    """A unique ID used to correlate this request to processing on your servers.

    Note: Courier does not verify the uniqueness of this ID.
    """

    utm: Optional[Utm] = None
    """
    Identify the campaign that refers traffic to a specific website, and attributes
    the browser's website session.
    """


class Preferences(BaseModel):
    subscription_topic_id: str
    """The ID of the subscription topic you want to apply to the message.

    If this is a templated message, it will override the subscription topic if
    already associated
    """


class ProvidersMetadata(BaseModel):
    utm: Optional[Utm] = None


class Providers(BaseModel):
    if_: Optional[str] = FieldInfo(alias="if", default=None)
    """
    A JavaScript conditional expression to determine if the message should be sent
    through the provider. Has access to the data and profile object. Only applies
    when a custom routing strategy is defined. For example,
    `data.name === profile.name`
    """

    metadata: Optional[ProvidersMetadata] = None

    override: Optional[Dict[str, object]] = None
    """Provider specific overrides."""

    timeouts: Optional[int] = None


class Routing(BaseModel):
    channels: List["MessageRoutingChannel"]
    """A list of channels or providers to send the message through.

    Can also recursively define sub-routing methods, which can be useful for
    defining advanced push notification delivery strategies.
    """

    method: Literal["all", "single"]


class Timeout(BaseModel):
    channel: Optional[Dict[str, int]] = None

    criteria: Optional[Literal["no-escalation", "delivered", "viewed", "engaged"]] = None

    escalation: Optional[int] = None

    message: Optional[int] = None

    provider: Optional[Dict[str, int]] = None


class BaseMessage(BaseModel):
    brand_id: Optional[str] = None

    channels: Optional[Dict[str, Channels]] = None
    """\"Define run-time configuration for one or more channels.

    If you don't specify channels, the default configuration for each channel will
    be used. Valid ChannelId's are: email, sms, push, inbox, direct_message, banner,
    and webhook."
    """

    context: Optional[MessageContext] = None
    """Context to load with this recipient.

    Will override any context set on message.context.
    """

    data: Optional[Dict[str, object]] = None
    """
    An arbitrary object that includes any data you want to pass to the message. The
    data will populate the corresponding template or elements variables.
    """

    delay: Optional[Delay] = None
    """Defines the time to wait before delivering the message.

    You can specify one of the following options. Duration with the number of
    milliseconds to delay. Until with an ISO 8601 timestamp that specifies when it
    should be delivered. Until with an OpenStreetMap opening_hours-like format that
    specifies the
    [Delivery Window](https://www.courier.com/docs/platform/sending/failover/#delivery-window)
    (e.g., 'Mo-Fr 08:00-18:00pm')
    """

    expiry: Optional[Expiry] = None
    """
    "Expiry allows you to set an absolute or relative time in which a message
    expires. Note: This is only valid for the Courier Inbox channel as of
    12-08-2022."
    """

    metadata: Optional[Metadata] = None
    """
    Metadata such as utm tracking attached with the notification through this
    channel.
    """

    preferences: Optional[Preferences] = None

    providers: Optional[Dict[str, Providers]] = None
    """An object whose keys are valid provider identifiers which map to an object."""

    routing: Optional[Routing] = None
    """
    Allows you to customize which channel(s) Courier will potentially deliver the
    message. If no routing key is specified, Courier will use the default routing
    configuration or routing defined by the template.
    """

    timeout: Optional[Timeout] = None
    """
    Time in ms to attempt the channel before failing over to the next available
    channel.
    """


from .message_routing_channel import MessageRoutingChannel
