# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SendToMsTeamsConversationID"]


class SendToMsTeamsConversationID(BaseModel):
    conversation_id: str

    service_url: str

    tenant_id: str
