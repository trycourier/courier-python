# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List as TypingList

from .._models import BaseModel
from .shared.list import List as SharedList
from .shared.paging import Paging

__all__ = ["ListListResponse"]


class ListListResponse(BaseModel):
    items: TypingList[SharedList]

    paging: Paging
