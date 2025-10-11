# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.put_subscriptions_recipient import PutSubscriptionsRecipient

__all__ = ["SubscriptionSubscribeParams"]


class SubscriptionSubscribeParams(TypedDict, total=False):
    recipients: Required[Iterable[PutSubscriptionsRecipient]]
