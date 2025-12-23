# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ListPatternRecipient"]


class ListPatternRecipient(TypedDict, total=False):
    """Send to users in lists matching a pattern"""

    data: Optional[Dict[str, object]]

    list_pattern: Optional[str]
