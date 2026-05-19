# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from a prior response."""

    limit: int
    """Page size. Minimum 1, maximum 100."""
