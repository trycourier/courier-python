# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["JourneyRetrieveParams"]


class JourneyRetrieveParams(TypedDict, total=False):
    version: str
    """Version selector: `draft`, `published` (default), or `vN`."""
