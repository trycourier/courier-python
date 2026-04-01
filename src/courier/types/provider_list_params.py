# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProviderListParams"]


class ProviderListParams(TypedDict, total=False):
    cursor: str
    """Opaque cursor for fetching the next page."""
