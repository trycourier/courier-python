# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SendMessageResponse"]


class SendMessageResponse(BaseModel):
    request_id: str = FieldInfo(alias="requestId")
    """
    A successful call to `POST /send` returns a `202` status code along with a
    `requestId` in the response body.

    For send requests that have a single recipient, the `requestId` is assigned to
    the derived message as its message_id. Therefore the `requestId` can be supplied
    to the Message's API for single recipient messages.

    For send requests that have multiple recipients (accounts, audiences, lists,
    etc.), Courier assigns a unique id to each derived message as its `message_id`.
    Therefore the `requestId` cannot be supplied to the Message's API for
    single-recipient messages.
    """
