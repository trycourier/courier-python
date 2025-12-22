# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SendToSlackChannel"]


class SendToSlackChannel(BaseModel):
    access_token: str

    channel: str
