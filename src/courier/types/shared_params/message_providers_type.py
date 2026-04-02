# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .metadata import Metadata

__all__ = ["MessageProvidersType"]

_MessageProvidersTypeReservedKeywords = TypedDict(
    "_MessageProvidersTypeReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class MessageProvidersType(_MessageProvidersTypeReservedKeywords, total=False):
    metadata: Optional[Metadata]

    override: Optional[Dict[str, object]]
    """Provider-specific overrides."""

    timeouts: Optional[int]
