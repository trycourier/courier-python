# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MsTeamsBaseProperties"]


class MsTeamsBaseProperties(BaseModel):
    """Tenant context shared by every MS Teams send variant.

    Provide at least one of `tenant_id` or `service_url`. If you provide both, they must agree — a `service_url` pointing at a different Microsoft tenant than `tenant_id` is rejected.
    """

    service_url: Optional[str] = None

    tenant_id: Optional[str] = None
