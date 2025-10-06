# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .lists.recipient_preferences_param import RecipientPreferencesParam

__all__ = ["ListUpdateParams"]


class ListUpdateParams(TypedDict, total=False):
    name: Required[str]

    preferences: Optional[RecipientPreferencesParam]
