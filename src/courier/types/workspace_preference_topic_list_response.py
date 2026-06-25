# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .workspace_preference_topic_get_response import WorkspacePreferenceTopicGetResponse

__all__ = ["WorkspacePreferenceTopicListResponse"]


class WorkspacePreferenceTopicListResponse(BaseModel):
    """Topics contained in a workspace preference."""

    results: List[WorkspacePreferenceTopicGetResponse]
