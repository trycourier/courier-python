# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NotificationListParams"]


class NotificationListParams(TypedDict, total=False):
    cursor: Optional[str]

    notes: Optional[bool]
    """Retrieve the notes from the Notification template settings."""
