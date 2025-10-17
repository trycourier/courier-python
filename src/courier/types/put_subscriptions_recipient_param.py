# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.recipient_preferences import RecipientPreferences

__all__ = ["PutSubscriptionsRecipientParam"]


class PutSubscriptionsRecipientParam(TypedDict, total=False):
    recipient_id: Required[Annotated[str, PropertyInfo(alias="recipientId")]]

    preferences: Optional[RecipientPreferences]
