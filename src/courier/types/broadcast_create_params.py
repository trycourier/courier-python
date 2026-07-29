# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BroadcastCreateParams"]


class BroadcastCreateParams(TypedDict, total=False):
    channel: Required[Literal["email", "sms", "push", "inbox", "slack", "msteams"]]
    """The single delivery channel for this broadcast."""

    name: Required[str]
    """Human-readable name."""
