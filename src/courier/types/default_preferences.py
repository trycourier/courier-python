# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .subscription_topic_new import SubscriptionTopicNew

__all__ = ["DefaultPreferences", "Item"]


class Item(SubscriptionTopicNew):
    id: str
    """Topic ID"""


class DefaultPreferences(BaseModel):
    items: Optional[List[Item]] = None
