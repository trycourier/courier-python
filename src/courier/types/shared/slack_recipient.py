# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .slack import Slack
from ..._models import BaseModel

__all__ = ["SlackRecipient"]


class SlackRecipient(BaseModel):
    """Send via Slack (channel, email, or user_id)"""

    slack: Slack
