# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .send_to_ms_teams_email import SendToMsTeamsEmail
from .send_to_ms_teams_user_id import SendToMsTeamsUserID
from .send_to_ms_teams_channel_id import SendToMsTeamsChannelID
from .send_to_ms_teams_channel_name import SendToMsTeamsChannelName
from .send_to_ms_teams_conversation_id import SendToMsTeamsConversationID

__all__ = ["MsTeams"]

MsTeams: TypeAlias = Union[
    SendToMsTeamsUserID,
    SendToMsTeamsEmail,
    SendToMsTeamsChannelID,
    SendToMsTeamsConversationID,
    SendToMsTeamsChannelName,
]
