# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .slack import Slack

__all__ = ["SlackRecipient"]


class SlackRecipient(TypedDict, total=False):
    """Send via Slack (channel, email, or user_id)"""

    slack: Required[Slack]
