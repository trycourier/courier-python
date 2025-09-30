# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..paging import Paging
from ..._models import BaseModel
from .topic_preference import TopicPreference

__all__ = ["PreferenceRetrieveResponse"]


class PreferenceRetrieveResponse(BaseModel):
    items: List[TopicPreference]
    """The Preferences associated with the user_id."""

    paging: Paging
    """Deprecated - Paging not implemented on this endpoint"""
