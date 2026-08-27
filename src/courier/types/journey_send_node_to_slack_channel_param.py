# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["JourneySendNodeToSlackChannelParam"]


class JourneySendNodeToSlackChannelParam(TypedDict, total=False):
    channel: Required[str]
    """Slack channel to send to, by name or ID."""

    access_token: str
    """A runtime reference to a Slack access token, such as `{{data.slack_token}}`.

    Literal values are rejected — they'd be stored permanently with no way to rotate
    them. Omit to use the token on the recipient's stored Slack profile.
    """
