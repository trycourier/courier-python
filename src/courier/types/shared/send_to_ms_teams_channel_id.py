# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SendToMsTeamsChannelID"]


class SendToMsTeamsChannelID(BaseModel):
    channel_id: str

    service_url: str

    tenant_id: str
