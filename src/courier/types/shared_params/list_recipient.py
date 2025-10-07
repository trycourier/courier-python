# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ListRecipient"]


class ListRecipient(TypedDict, total=False):
    data: Optional[Dict[str, object]]

    list_id: Optional[str]
