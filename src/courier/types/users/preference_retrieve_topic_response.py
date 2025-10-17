# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .topic_preference import TopicPreference

__all__ = ["PreferenceRetrieveTopicResponse"]


class PreferenceRetrieveTopicResponse(BaseModel):
    topic: TopicPreference
