# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .audit_event import AuditEvent
from .shared.paging import Paging

__all__ = ["AuditEventListResponse"]


class AuditEventListResponse(BaseModel):
    paging: Paging

    results: List[AuditEvent]
