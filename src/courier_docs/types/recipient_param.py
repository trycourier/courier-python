# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .user_recipient_param import UserRecipientParam
from .slack_base_properties_param import SlackBasePropertiesParam
from .ms_teams_base_properties_param import MsTeamsBasePropertiesParam

__all__ = [
    "RecipientParam",
    "AudienceRecipient",
    "AudienceRecipientFilter",
    "UnionMember1",
    "UnionMember1Filter",
    "UnionMember2",
    "SlackRecipient",
    "SlackRecipientSlackSendToSlackChannel",
    "SlackRecipientSlackSendToSlackEmail",
    "SlackRecipientSlackSendToSlackUserID",
    "MsTeamsRecipient",
    "MsTeamsRecipientMsTeamsSendToMsTeamsUserID",
    "MsTeamsRecipientMsTeamsSendToMsTeamsEmail",
    "MsTeamsRecipientMsTeamsSendToMsTeamsChannelID",
    "MsTeamsRecipientMsTeamsSendToMsTeamsConversationID",
    "MsTeamsRecipientMsTeamsSendToMsTeamsChannelName",
    "PagerdutyRecipient",
    "PagerdutyRecipientPagerduty",
    "WebhookRecipient",
    "WebhookRecipientWebhook",
    "WebhookRecipientWebhookAuthentication",
]


class AudienceRecipientFilter(TypedDict, total=False):
    operator: Required[Literal["MEMBER_OF"]]
    """Send to users only if they are member of the account"""

    path: Required[Literal["account_id"]]

    value: Required[str]


class AudienceRecipient(TypedDict, total=False):
    audience_id: Required[str]
    """A unique identifier associated with an Audience.

    A message will be sent to each user in the audience.
    """

    data: Optional[Dict[str, object]]

    filters: Optional[Iterable[AudienceRecipientFilter]]


class UnionMember1Filter(TypedDict, total=False):
    operator: Required[Literal["MEMBER_OF"]]
    """Send to users only if they are member of the account"""

    path: Required[Literal["account_id"]]

    value: Required[str]


class UnionMember1(TypedDict, total=False):
    data: Optional[Dict[str, object]]

    filters: Optional[Iterable[UnionMember1Filter]]

    list_id: Optional[str]


class UnionMember2(TypedDict, total=False):
    data: Optional[Dict[str, object]]

    list_pattern: Optional[str]


class SlackRecipientSlackSendToSlackChannel(SlackBasePropertiesParam, total=False):
    channel: Required[str]


class SlackRecipientSlackSendToSlackEmail(SlackBasePropertiesParam, total=False):
    email: Required[str]


class SlackRecipientSlackSendToSlackUserID(SlackBasePropertiesParam, total=False):
    user_id: Required[str]


class SlackRecipient(TypedDict, total=False):
    slack: Required[
        Union[
            SlackRecipientSlackSendToSlackChannel,
            SlackRecipientSlackSendToSlackEmail,
            SlackRecipientSlackSendToSlackUserID,
        ]
    ]


class MsTeamsRecipientMsTeamsSendToMsTeamsUserID(MsTeamsBasePropertiesParam, total=False):
    user_id: Required[str]


class MsTeamsRecipientMsTeamsSendToMsTeamsEmail(MsTeamsBasePropertiesParam, total=False):
    email: Required[str]


class MsTeamsRecipientMsTeamsSendToMsTeamsChannelID(MsTeamsBasePropertiesParam, total=False):
    channel_id: Required[str]


class MsTeamsRecipientMsTeamsSendToMsTeamsConversationID(MsTeamsBasePropertiesParam, total=False):
    conversation_id: Required[str]


class MsTeamsRecipientMsTeamsSendToMsTeamsChannelName(MsTeamsBasePropertiesParam, total=False):
    channel_name: Required[str]

    team_id: Required[str]


class MsTeamsRecipient(TypedDict, total=False):
    ms_teams: Required[
        Union[
            MsTeamsRecipientMsTeamsSendToMsTeamsUserID,
            MsTeamsRecipientMsTeamsSendToMsTeamsEmail,
            MsTeamsRecipientMsTeamsSendToMsTeamsChannelID,
            MsTeamsRecipientMsTeamsSendToMsTeamsConversationID,
            MsTeamsRecipientMsTeamsSendToMsTeamsChannelName,
        ]
    ]


class PagerdutyRecipientPagerduty(TypedDict, total=False):
    event_action: Optional[str]

    routing_key: Optional[str]

    severity: Optional[str]

    source: Optional[str]


class PagerdutyRecipient(TypedDict, total=False):
    pagerduty: Required[PagerdutyRecipientPagerduty]


class WebhookRecipientWebhookAuthentication(TypedDict, total=False):
    mode: Required[Literal["none", "basic", "bearer"]]
    """The authentication mode to use. Defaults to 'none' if not specified."""

    token: Optional[str]
    """Token for bearer authentication."""

    password: Optional[str]
    """Password for basic authentication."""

    username: Optional[str]
    """Username for basic authentication."""


class WebhookRecipientWebhook(TypedDict, total=False):
    url: Required[str]
    """The URL to send the webhook request to."""

    authentication: Optional[WebhookRecipientWebhookAuthentication]
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


class WebhookRecipient(TypedDict, total=False):
    webhook: Required[WebhookRecipientWebhook]


RecipientParam: TypeAlias = Union[
    AudienceRecipient,
    UnionMember1,
    UnionMember2,
    UserRecipientParam,
    SlackRecipient,
    MsTeamsRecipient,
    Dict[str, object],
    PagerdutyRecipient,
    WebhookRecipient,
]
