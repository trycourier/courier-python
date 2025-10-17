# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .inbound_bulk_message_param import InboundBulkMessageParam

__all__ = ["BulkCreateJobParams"]


class BulkCreateJobParams(TypedDict, total=False):
    message: Required[InboundBulkMessageParam]
