# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NotificationListParams"]


class NotificationListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque pagination cursor from a previous response. Omit for the first page."""

    event_id: str
    """Filter to templates linked to this event map ID."""

    notes: Optional[bool]
    """Include template notes in the response. Only applies to legacy templates."""
