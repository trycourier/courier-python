# This file was auto-generated by Fern from our API Definition.

import typing

from .send_to_ms_teams_channel_id import SendToMsTeamsChannelId
from .send_to_ms_teams_channel_name import SendToMsTeamsChannelName
from .send_to_ms_teams_conversation_id import SendToMsTeamsConversationId
from .send_to_ms_teams_email import SendToMsTeamsEmail
from .send_to_ms_teams_user_id import SendToMsTeamsUserId

MsTeams = typing.Union[
    SendToMsTeamsUserId,
    SendToMsTeamsEmail,
    SendToMsTeamsChannelId,
    SendToMsTeamsConversationId,
    SendToMsTeamsChannelName,
]
