# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.preference_status import PreferenceStatus
from ..shared.channel_classification import ChannelClassification

__all__ = ["TopicPreference"]


class TopicPreference(BaseModel):
    default_status: PreferenceStatus

    status: PreferenceStatus

    topic_id: str

    topic_name: str

    custom_routing: Optional[List[ChannelClassification]] = None
    """The Channels a user has chosen to receive notifications through for this topic"""

    has_custom_routing: Optional[bool] = None
