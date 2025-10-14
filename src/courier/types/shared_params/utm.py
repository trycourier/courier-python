# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["Utm"]


class Utm(TypedDict, total=False):
    campaign: Optional[str]

    content: Optional[str]

    medium: Optional[str]

    source: Optional[str]

    term: Optional[str]
