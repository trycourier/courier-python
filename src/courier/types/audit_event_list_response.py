# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .paging import Paging
from .._models import BaseModel
from .audit_event import AuditEvent

__all__ = ["AuditEventListResponse"]


class AuditEventListResponse(BaseModel):
    paging: Paging

    results: List[AuditEvent]
