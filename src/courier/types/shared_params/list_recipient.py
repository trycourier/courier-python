# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import TypedDict

from .list_filter import ListFilter

__all__ = ["ListRecipient"]


class ListRecipient(TypedDict, total=False):
    """Send to all users in a specific list"""

    data: Optional[Dict[str, object]]

    filters: Optional[Iterable[ListFilter]]

    list_id: Optional[str]
