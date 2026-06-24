# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .preference_topic_get_response import PreferenceTopicGetResponse

__all__ = ["PreferenceTopicListResponse"]


class PreferenceTopicListResponse(BaseModel):
    """Topics contained in a preference section."""

    results: List[PreferenceTopicGetResponse]
