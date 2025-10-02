# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BulkRetrieveJobResponse", "Job"]


class Job(BaseModel):
    definition: "InboundBulkMessage"

    enqueued: int

    failures: int

    received: int

    status: Literal["CREATED", "PROCESSING", "COMPLETED", "ERROR"]


class BulkRetrieveJobResponse(BaseModel):
    job: Job


from .inbound_bulk_message import InboundBulkMessage
