# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.paging import Paging
from .inbound_bulk_message_user import InboundBulkMessageUser

__all__ = ["BulkListUsersResponse", "Item"]


class Item(InboundBulkMessageUser):
    status: Literal["PENDING", "ENQUEUED", "ERROR"]

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)


class BulkListUsersResponse(BaseModel):
    items: List[Item]

    paging: Paging
