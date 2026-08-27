# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SendToMsTeamsChannelName"]


class SendToMsTeamsChannelName(BaseModel):
    """`team_id` is required alongside `channel_name`.

    Also provide at least one of `tenant_id` or `service_url`; if you provide both, they must agree.
    """

    channel_name: str

    team_id: str

    service_url: Optional[str] = None

    tenant_id: Optional[str] = None
