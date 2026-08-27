# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["JourneySendNodeToSlackEmail"]


class JourneySendNodeToSlackEmail(BaseModel):
    email: str
    """
    Email address of the Slack user to send to, resolved via the workspace
    directory.
    """

    access_token: Optional[str] = None
    """A runtime reference to a Slack access token, such as `{{data.slack_token}}`.

    Literal values are rejected — they'd be stored permanently with no way to rotate
    them. Omit to use the token on the recipient's stored Slack profile.
    """
