# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NotificationListVersionsParams"]


class NotificationListVersionsParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor from a previous response. Omit for the first page."""

    limit: int
    """Maximum number of versions to return per page. Default 10, max 10."""
