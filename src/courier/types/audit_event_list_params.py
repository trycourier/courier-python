# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AuditEventListParams"]


class AuditEventListParams(TypedDict, total=False):
    cursor: Optional[str]
    """A unique identifier that allows for fetching the next set of audit events."""
