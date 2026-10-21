# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ProviderPatchParams"]


class ProviderPatchParams(TypedDict, total=False):
    alias: Optional[str]
    """Updated alias. Set to null to clear it."""

    provider: str
    """The provider key identifying the type.

    Optional. When sent, it must match the stored provider, otherwise the request
    returns a 400.
    """

    settings: Dict[str, object]
    """
    Provider-specific settings (snake_case keys) to merge into the stored settings,
    using JSON Merge Patch (RFC 7396). Each key you send replaces the stored value,
    a key set to null is removed, nested objects merge recursively, and arrays
    replace the stored value. Keys you omit keep their stored values. Set
    `rate_limit` to null to remove this configuration's send rate limit.
    """

    title: str
    """Updated display title."""
