# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuditEvent", "Actor"]


class Actor(BaseModel):
    id: str

    email: Optional[str] = None


class AuditEvent(BaseModel):
    actor: Actor

    audit_event_id: str = FieldInfo(alias="auditEventId")

    source: str

    target: str

    timestamp: str

    type: str
