# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MessageContextParam"]


class MessageContextParam(TypedDict, total=False):
    tenant_id: Optional[str]
    """
    An id of a tenant, see
    [tenants api docs](https://www.courier.com/docs/reference/tenants/). Will load
    brand, default preferences and any other base context data associated with this
    tenant.
    """
