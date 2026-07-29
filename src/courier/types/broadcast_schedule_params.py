# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BroadcastScheduleParams"]


class BroadcastScheduleParams(TypedDict, total=False):
    recipient_id: Required[str]
    """ID of the target list or audience."""

    recipient_type: Required[Literal["list", "audience"]]
    """Whether the broadcast targets a list or an audience."""

    scheduled_to: Required[str]
    """Wall-clock timestamp of the future send, no timezone offset (e.g.

    "2026-07-21T20:00:00"). The zone is given by `timezone`.
    """

    timezone: str
    """IANA timezone for the scheduled send (e.g. America/New_York)."""
