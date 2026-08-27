# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SendToMsTeamsChannelID"]


class SendToMsTeamsChannelID(BaseModel):
    """Sends directly to a Microsoft Teams channel by its Bot Framework ID.

    Still provide at least one of `tenant_id` or `service_url` — sends without either have failed Bot Framework authentication in testing.
    """

    channel_id: str

    service_url: Optional[str] = None

    tenant_id: Optional[str] = None
