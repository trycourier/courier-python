# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .inbound_bulk_message import InboundBulkMessage

__all__ = ["BulkRetrieveJobResponse", "Job"]


class Job(BaseModel):
    definition: InboundBulkMessage
    """Bulk message definition. Supports two formats:

    - V1 format: Requires `event` field (event ID or notification ID)
    - V2 format: Optionally use `template` (notification ID) or `content` (Elemental
      content) in addition to `event`
    """

    enqueued: int

    failures: int

    received: int

    status: Literal["CREATED", "PROCESSING", "COMPLETED", "ERROR"]


class BulkRetrieveJobResponse(BaseModel):
    job: Job
