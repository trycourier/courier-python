# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.paging import Paging
from .shared.audit_event import AuditEvent

__all__ = ["AuditEventListResponse"]


class AuditEventListResponse(BaseModel):
    paging: Paging

    results: List[AuditEvent]
