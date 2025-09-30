# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MessageHistoryParams"]


class MessageHistoryParams(TypedDict, total=False):
    type: Optional[str]
    """A supported Message History type that will filter the events returned."""
