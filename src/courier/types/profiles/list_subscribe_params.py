# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..subscribe_to_lists_request_item_param import SubscribeToListsRequestItemParam

__all__ = ["ListSubscribeParams"]


class ListSubscribeParams(TypedDict, total=False):
    lists: Required[Iterable[SubscribeToListsRequestItemParam]]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]
