# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .subscription_topic_new_param import SubscriptionTopicNewParam

__all__ = ["DefaultPreferencesParam", "Item"]


class Item(SubscriptionTopicNewParam, total=False):
    id: Required[str]
    """Topic ID"""


class DefaultPreferencesParam(TypedDict, total=False):
    items: Optional[Iterable[Item]]
