# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageResendResponse"]


class MessageResendResponse(BaseModel):
    message_id: str = FieldInfo(alias="messageId")
    """The new message id for the resent message.

    It is distinct from the id of the original message that was resent.
    """
