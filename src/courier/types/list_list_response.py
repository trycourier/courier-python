# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List as TypingList

from .list import List as ListList
from .paging import Paging
from .._models import BaseModel

__all__ = ["ListListResponse"]


class ListListResponse(BaseModel):
    items: TypingList[ListList]

    paging: Paging
