# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RoutingStrategyListParams"]


class RoutingStrategyListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque pagination cursor from a previous response. Omit for the first page."""

    limit: int
    """Maximum number of results per page. Default 20, max 100."""
