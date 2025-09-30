# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MessageContext"]


class MessageContext(BaseModel):
    tenant_id: Optional[str] = None
    """
    An id of a tenant, see
    [tenants api docs](https://www.courier.com/docs/reference/tenants/). Will load
    brand, default preferences and any other base context data associated with this
    tenant.
    """
