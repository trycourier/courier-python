# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.channel_classification import ChannelClassification
from .workspace_preference_topic_get_response import WorkspacePreferenceTopicGetResponse

__all__ = ["WorkspacePreferenceGetResponse"]


class WorkspacePreferenceGetResponse(BaseModel):
    """A workspace preference in your workspace, including its topics."""

    id: str
    """The workspace preference id."""

    created: str
    """ISO-8601 timestamp of when the workspace preference was created."""

    has_custom_routing: bool
    """Whether the workspace preference defines custom routing for its topics."""

    name: str
    """Human-readable name."""

    routing_options: List[ChannelClassification]
    """Default channels for the workspace preference. May be empty."""

    topics: List[WorkspacePreferenceTopicGetResponse]
    """The topics contained in this workspace preference."""

    creator: Optional[str] = None
    """Id of the creator."""

    updated: Optional[str] = None
    """ISO-8601 timestamp of the last update."""

    updater: Optional[str] = None
    """Id of the last updater."""
