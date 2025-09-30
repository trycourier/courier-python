# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PreferenceRetrieveTopicParams"]


class PreferenceRetrieveTopicParams(TypedDict, total=False):
    user_id: Required[str]

    tenant_id: Optional[str]
    """Query the preferences of a user for this specific tenant context."""
