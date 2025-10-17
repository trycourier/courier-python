# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.channel_classification import ChannelClassification

__all__ = ["SubscriptionTopicNew"]


class SubscriptionTopicNew(BaseModel):
    status: Literal["OPTED_OUT", "OPTED_IN", "REQUIRED"]

    custom_routing: Optional[List[ChannelClassification]] = None
    """The default channels to send to this tenant when has_custom_routing is enabled"""

    has_custom_routing: Optional[bool] = None
    """Override channel routing with custom preferences.

    This will override any template prefernces that are set, but a user can still
    customize their preferences
    """
