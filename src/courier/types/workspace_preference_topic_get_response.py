# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.channel_classification import ChannelClassification

__all__ = ["WorkspacePreferenceTopicGetResponse"]


class WorkspacePreferenceTopicGetResponse(BaseModel):
    """A subscription preference topic in your workspace."""

    id: str
    """The preference topic id."""

    allowed_preferences: List[Literal["snooze", "channel_preferences"]]
    """Preference controls a recipient may customize. May be empty."""

    created: str
    """ISO-8601 timestamp of when the topic was created."""

    default_status: Literal["OPTED_OUT", "OPTED_IN", "REQUIRED"]
    """The default subscription status applied when a recipient has not set their own."""

    include_unsubscribe_header: bool
    """Whether a list-unsubscribe header is included on emails for this topic."""

    name: str
    """Human-readable name."""

    routing_options: List[ChannelClassification]
    """Default channels delivered for this topic. May be empty."""

    topic_data: Dict[str, object]
    """Arbitrary metadata associated with the topic."""

    updated: str
    """ISO-8601 timestamp of the last update."""

    creator: Optional[str] = None
    """Id of the creator."""

    description: Optional[str] = None
    """Optional description shown under the topic on the hosted preferences page."""

    updater: Optional[str] = None
    """Id of the last updater."""
