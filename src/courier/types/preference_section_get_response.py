# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .preference_topic_get_response import PreferenceTopicGetResponse
from .shared.channel_classification import ChannelClassification

__all__ = ["PreferenceSectionGetResponse"]


class PreferenceSectionGetResponse(BaseModel):
    """A preference section in your workspace, including its topics."""

    id: str
    """The preference section id."""

    created: str
    """ISO-8601 timestamp of when the section was created."""

    has_custom_routing: bool
    """Whether the section defines custom routing for its topics."""

    name: str
    """Human-readable name."""

    routing_options: List[ChannelClassification]
    """Default channels for the section. May be empty."""

    topics: List[PreferenceTopicGetResponse]
    """The topics contained in this section."""

    creator: Optional[str] = None
    """Id of the creator."""

    updated: Optional[str] = None
    """ISO-8601 timestamp of the last update."""

    updater: Optional[str] = None
    """Id of the last updater."""
