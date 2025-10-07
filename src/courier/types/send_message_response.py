# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SendMessageResponse"]


class SendMessageResponse(BaseModel):
    request_id: str = FieldInfo(alias="requestId")
    """
    A successful call to `POST /send` returns a `202` status code along with a
    `requestId` in the response body. For single-recipient requests, the `requestId`
    is the derived message_id. For multiple recipients, Courier assigns a unique
    message_id to each derived message.
    """
