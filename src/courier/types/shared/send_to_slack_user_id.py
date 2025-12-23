# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SendToSlackUserID"]


class SendToSlackUserID(BaseModel):
    access_token: str

    user_id: str
