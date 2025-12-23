# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .send_to_slack_email import SendToSlackEmail
from .send_to_slack_channel import SendToSlackChannel
from .send_to_slack_user_id import SendToSlackUserID

__all__ = ["Slack"]

Slack: TypeAlias = Union[SendToSlackChannel, SendToSlackEmail, SendToSlackUserID]
