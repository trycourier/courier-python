# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.channel_classification import ChannelClassification

__all__ = ["BulkPreferenceTopic"]


class BulkPreferenceTopic(BaseModel):
    """A single topic override echoed in a bulk preference response."""

    custom_routing: List[ChannelClassification]

    has_custom_routing: bool

    status: Literal["OPTED_IN", "OPTED_OUT"]
    """The applied subscription status.

    Echoes the requested value, so it is always OPTED_IN or OPTED_OUT.
    """

    topic_id: str
