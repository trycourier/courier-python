# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SendToMsTeamsUserID"]


class SendToMsTeamsUserID(BaseModel):
    service_url: str

    tenant_id: str

    user_id: str
