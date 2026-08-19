# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    cursor: str
    """A cursor token for pagination.

    Use the `next_cursor` from the previous response to fetch the next page of
    results. Treat it as opaque.
    """

    end_date: str
    """An inclusive upper bound on `created_at`, in the same format as `start_date`."""

    limit: str
    """The number of runs to return per page, between `1` and `50`.

    Defaults to `20`. Values outside the range are clamped, and a non-numeric value
    falls back to `20`.
    """

    start_date: str
    """An inclusive lower bound on `created_at`, as an ISO 8601 date or timestamp (e.g.

    `2026-08-18` or `2026-08-18T20:06:36.259Z`). Any other format returns `400`.
    """

    status: str
    """A comma-separated list of run statuses to filter on, e.g. `PROCESSED,ERROR`."""

    template_id: str
    """A comma-separated list of Automation Template ids to filter on."""
