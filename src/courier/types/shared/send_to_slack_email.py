# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SendToSlackEmail"]


class SendToSlackEmail(BaseModel):
    access_token: str

    email: str
