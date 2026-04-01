# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CatalogListParams"]


class CatalogListParams(TypedDict, total=False):
    channel: str
    """Exact match (case-insensitive) against the provider channel taxonomy (e.g.

    `email`, `sms`, `push`).
    """

    keys: str
    """Comma-separated provider keys to filter by (e.g. `sendgrid,twilio`)."""

    name: str
    """Case-insensitive substring match against the provider display name."""
