# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ProviderUpdateParams"]


class ProviderUpdateParams(TypedDict, total=False):
    provider: Required[str]
    """The provider key identifying the type."""

    alias: str
    """Updated alias. Omit to clear."""

    settings: Dict[str, object]
    """Provider-specific settings (snake_case keys).

    Replaces the full settings object — omitted settings fields are removed. Use the
    catalog endpoint to check required fields.
    """

    title: str
    """Updated display title."""
