# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..subscribe_to_lists_request_item_param import SubscribeToListsRequestItemParam

__all__ = ["ListSubscribeParams"]


class ListSubscribeParams(TypedDict, total=False):
    lists: Required[Iterable[SubscribeToListsRequestItemParam]]
