# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .broadcast_schedule import BroadcastSchedule

__all__ = ["Broadcast"]


class Broadcast(BaseModel):
    """
    A broadcast — a single-channel message delivered to a known set of recipients (a list or audience).
    """

    id: str
    """The broadcast ID (bst\\__ prefix)."""

    channel: Literal["email", "sms", "push", "inbox", "slack", "msteams"]
    """The broadcast's delivery channel."""

    created_at: str
    """ISO 8601 timestamp when the broadcast was created."""

    created_by: str
    """Actor that created the broadcast."""

    name: str
    """Human-readable name."""

    status: Literal["draft", "scheduled", "sending", "sent"]
    """Lifecycle status of the broadcast."""

    updated_at: str
    """ISO 8601 timestamp of the last update."""

    updated_by: str
    """Actor that last updated the broadcast."""

    archived_at: Optional[str] = None
    """ISO 8601 timestamp when the broadcast was archived, if archived."""

    archived_by: Optional[str] = None
    """Actor that archived the broadcast, if archived."""

    schedule: Optional[BroadcastSchedule] = None
    """The delivery schedule and recipient targeting for a broadcast."""
