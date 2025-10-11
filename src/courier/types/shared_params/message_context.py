# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MessageContext"]


class MessageContext(TypedDict, total=False):
    tenant_id: Optional[str]
    """Tenant id used to load brand/default preferences/context."""
