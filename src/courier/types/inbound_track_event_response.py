# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InboundTrackEventResponse"]


class InboundTrackEventResponse(BaseModel):
    message_id: str = FieldInfo(alias="messageId")
    """
    A successful call returns a `202` status code along with a `requestId` in the
    response body.
    """
