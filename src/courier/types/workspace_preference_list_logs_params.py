# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkspacePreferenceListLogsParams"]


class WorkspacePreferenceListLogsParams(TypedDict, total=False):
    cursor: str
    """A cursor from a previous response's paging.cursor.

    Continue only while paging.more is true; the cursor is omitted on the last page.
    """

    limit: int
    """How many entries to return. Defaults to 25."""

    since: str
    """Return only changes at or after this time, as an ISO-8601 date or date-time.

    A date alone is read as the start of that day in UTC.
    """

    tenant_id: str
    """Narrow to the changes this user made in one tenant context.

    Only valid together with user_id.
    """

    user_id: str
    """Return only this user's changes.

    Omit it to read every change in the environment.
    """
