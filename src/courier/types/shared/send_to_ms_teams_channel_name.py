# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SendToMsTeamsChannelName"]


class SendToMsTeamsChannelName(BaseModel):
    channel_name: str

    service_url: str

    team_id: str

    tenant_id: str
