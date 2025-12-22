# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .intercom_recipient import IntercomRecipient

__all__ = ["Intercom"]


class Intercom(BaseModel):
    from_: str = FieldInfo(alias="from")

    to: IntercomRecipient
