# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MessageContext"]


class MessageContext(BaseModel):
    tenant_id: Optional[str] = None
    """Tenant id used to load brand/default preferences/context."""
