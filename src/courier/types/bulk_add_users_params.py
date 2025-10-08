# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.inbound_bulk_message_user import InboundBulkMessageUser

__all__ = ["BulkAddUsersParams"]


class BulkAddUsersParams(TypedDict, total=False):
    users: Required[Iterable[InboundBulkMessageUser]]
