# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .recipient_param import RecipientParam
from .user_recipient_param import UserRecipientParam
from .slack_base_properties_param import SlackBasePropertiesParam
from .ms_teams_base_properties_param import MsTeamsBasePropertiesParam

__all__ = [
    "BaseMessageSendToParam",
    "To",
    "ToAudienceRecipient",
    "ToAudienceRecipientFilter",
    "ToUnionMember1",
    "ToUnionMember1Filter",
    "ToUnionMember2",
    "ToSlackRecipient",
    "ToSlackRecipientSlackSendToSlackChannel",
    "ToSlackRecipientSlackSendToSlackEmail",
    "ToSlackRecipientSlackSendToSlackUserID",
    "ToMsTeamsRecipient",
    "ToMsTeamsRecipientMsTeamsSendToMsTeamsUserID",
    "ToMsTeamsRecipientMsTeamsSendToMsTeamsEmail",
    "ToMsTeamsRecipientMsTeamsSendToMsTeamsChannelID",
    "ToMsTeamsRecipientMsTeamsSendToMsTeamsConversationID",
    "ToMsTeamsRecipientMsTeamsSendToMsTeamsChannelName",
    "ToPagerdutyRecipient",
    "ToPagerdutyRecipientPagerduty",
    "ToWebhookRecipient",
    "ToWebhookRecipientWebhook",
    "ToWebhookRecipientWebhookAuthentication",
]


class ToAudienceRecipientFilter(TypedDict, total=False):
    operator: Required[Literal["MEMBER_OF"]]
    """Send to users only if they are member of the account"""

    path: Required[Literal["account_id"]]

    value: Required[str]


class ToAudienceRecipient(TypedDict, total=False):
    audience_id: Required[str]
    """A unique identifier associated with an Audience.

    A message will be sent to each user in the audience.
    """

    data: Optional[Dict[str, object]]

    filters: Optional[Iterable[ToAudienceRecipientFilter]]


class ToUnionMember1Filter(TypedDict, total=False):
    operator: Required[Literal["MEMBER_OF"]]
    """Send to users only if they are member of the account"""

    path: Required[Literal["account_id"]]

    value: Required[str]


class ToUnionMember1(TypedDict, total=False):
    data: Optional[Dict[str, object]]

    filters: Optional[Iterable[ToUnionMember1Filter]]

    list_id: Optional[str]


class ToUnionMember2(TypedDict, total=False):
    data: Optional[Dict[str, object]]

    list_pattern: Optional[str]


class ToSlackRecipientSlackSendToSlackChannel(SlackBasePropertiesParam, total=False):
    channel: Required[str]


class ToSlackRecipientSlackSendToSlackEmail(SlackBasePropertiesParam, total=False):
    email: Required[str]


class ToSlackRecipientSlackSendToSlackUserID(SlackBasePropertiesParam, total=False):
    user_id: Required[str]


class ToSlackRecipient(TypedDict, total=False):
    slack: Required[
        Union[
            ToSlackRecipientSlackSendToSlackChannel,
            ToSlackRecipientSlackSendToSlackEmail,
            ToSlackRecipientSlackSendToSlackUserID,
        ]
    ]


class ToMsTeamsRecipientMsTeamsSendToMsTeamsUserID(MsTeamsBasePropertiesParam, total=False):
    user_id: Required[str]


class ToMsTeamsRecipientMsTeamsSendToMsTeamsEmail(MsTeamsBasePropertiesParam, total=False):
    email: Required[str]


class ToMsTeamsRecipientMsTeamsSendToMsTeamsChannelID(MsTeamsBasePropertiesParam, total=False):
    channel_id: Required[str]


class ToMsTeamsRecipientMsTeamsSendToMsTeamsConversationID(MsTeamsBasePropertiesParam, total=False):
    conversation_id: Required[str]


class ToMsTeamsRecipientMsTeamsSendToMsTeamsChannelName(MsTeamsBasePropertiesParam, total=False):
    channel_name: Required[str]

    team_id: Required[str]


class ToMsTeamsRecipient(TypedDict, total=False):
    ms_teams: Required[
        Union[
            ToMsTeamsRecipientMsTeamsSendToMsTeamsUserID,
            ToMsTeamsRecipientMsTeamsSendToMsTeamsEmail,
            ToMsTeamsRecipientMsTeamsSendToMsTeamsChannelID,
            ToMsTeamsRecipientMsTeamsSendToMsTeamsConversationID,
            ToMsTeamsRecipientMsTeamsSendToMsTeamsChannelName,
        ]
    ]


class ToPagerdutyRecipientPagerduty(TypedDict, total=False):
    event_action: Optional[str]

    routing_key: Optional[str]

    severity: Optional[str]

    source: Optional[str]


class ToPagerdutyRecipient(TypedDict, total=False):
    pagerduty: Required[ToPagerdutyRecipientPagerduty]


class ToWebhookRecipientWebhookAuthentication(TypedDict, total=False):
    mode: Required[Literal["none", "basic", "bearer"]]
    """The authentication mode to use. Defaults to 'none' if not specified."""

    token: Optional[str]
    """Token for bearer authentication."""

    password: Optional[str]
    """Password for basic authentication."""

    username: Optional[str]
    """Username for basic authentication."""


class ToWebhookRecipientWebhook(TypedDict, total=False):
    url: Required[str]
    """The URL to send the webhook request to."""

    authentication: Optional[ToWebhookRecipientWebhookAuthentication]
    """Authentication configuration for the webhook request."""

    headers: Optional[Dict[str, str]]
    """Custom headers to include in the webhook request."""

    method: Optional[Literal["POST", "PUT"]]
    """The HTTP method to use for the webhook request.

    Defaults to POST if not specified.
    """

    profile: Optional[Literal["limited", "expanded"]]
    """Specifies what profile information is included in the request payload.

    Defaults to 'limited' if not specified.
    """


class ToWebhookRecipient(TypedDict, total=False):
    webhook: Required[ToWebhookRecipientWebhook]


To: TypeAlias = Union[
    ToAudienceRecipient,
    ToUnionMember1,
    ToUnionMember2,
    UserRecipientParam,
    ToSlackRecipient,
    ToMsTeamsRecipient,
    Dict[str, object],
    ToPagerdutyRecipient,
    ToWebhookRecipient,
    Iterable[RecipientParam],
]


class BaseMessageSendToParam(TypedDict, total=False):
    to: Optional[To]
    """The recipient or a list of recipients of the message"""
