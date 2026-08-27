# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["JourneySendNodeToSlackUserID"]


class JourneySendNodeToSlackUserID(BaseModel):
    user_id: str
    """Slack user ID to send to."""

    access_token: Optional[str] = None
    """A runtime reference to a Slack access token, such as `{{data.slack_token}}`.

    Literal values are rejected — they'd be stored permanently with no way to rotate
    them. Omit to use the token on the recipient's stored Slack profile.
    """
