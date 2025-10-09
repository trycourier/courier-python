# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.paging import Paging
from .shared.user_list import UserList

__all__ = ["ListListResponse"]


class ListListResponse(BaseModel):
    items: List[UserList]

    paging: Paging
