# This file was auto-generated by Fern from our API Definition.

import typing

from .audience_recipient import AudienceRecipient
from .list_pattern_recipient import ListPatternRecipient
from .list_recipient import ListRecipient
from .ms_teams_recipient import MsTeamsRecipient
from .pagerduty_recipient import PagerdutyRecipient
from .recipient_data import RecipientData
from .slack_recipient import SlackRecipient
from .user_recipient import UserRecipient
from .webhook_recipient import WebhookRecipient

Recipient = typing.Union[
    AudienceRecipient,
    ListRecipient,
    ListPatternRecipient,
    UserRecipient,
    SlackRecipient,
    MsTeamsRecipient,
    RecipientData,
    PagerdutyRecipient,
    WebhookRecipient,
]
