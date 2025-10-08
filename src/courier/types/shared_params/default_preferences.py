# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .subscription_topic_new import SubscriptionTopicNew

__all__ = ["DefaultPreferences", "Item"]


class Item(SubscriptionTopicNew, total=False):
    id: Required[str]
    """Topic ID"""


class DefaultPreferences(TypedDict, total=False):
    items: Optional[Iterable[Item]]
