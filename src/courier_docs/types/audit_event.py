# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuditEvent", "Actor", "Target"]


class Actor(BaseModel):
    id: Optional[str] = None

    email: Optional[str] = None


class Target(BaseModel):
    id: Optional[str] = None

    email: Optional[str] = None


class AuditEvent(BaseModel):
    audit_event_id: str = FieldInfo(alias="auditEventId")

    source: str

    timestamp: str

    type: str

    actor: Optional[Actor] = None

    target: Optional[Target] = None
