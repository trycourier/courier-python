# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SendToMsTeamsEmail"]


class SendToMsTeamsEmail(BaseModel):
    """Provide at least one of `tenant_id` or `service_url`.

    If you provide both, they must agree.
    """

    email: str

    service_url: Optional[str] = None

    tenant_id: Optional[str] = None
