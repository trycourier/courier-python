# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BroadcastSchedule"]


class BroadcastSchedule(BaseModel):
    """The delivery schedule and recipient targeting for a broadcast."""

    recipient_id: str
    """ID of the target list or audience."""

    recipient_type: Literal["list", "audience"]
    """Whether the broadcast targets a list or an audience."""

    scheduled_to: Optional[str] = None
    """Wall-clock timestamp of the scheduled send, no timezone offset (e.g.

    "2026-07-21T20:00:00").
    """

    timezone: Optional[str] = None
    """IANA timezone for the scheduled send (e.g. America/New_York)."""
