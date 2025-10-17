# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.paging import Paging
from .subscription_list import SubscriptionList

__all__ = ["ListListResponse"]


class ListListResponse(BaseModel):
    items: List[SubscriptionList]

    paging: Paging
