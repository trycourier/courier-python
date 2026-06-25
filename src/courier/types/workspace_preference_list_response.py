# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .workspace_preference_get_response import WorkspacePreferenceGetResponse

__all__ = ["WorkspacePreferenceListResponse"]


class WorkspacePreferenceListResponse(BaseModel):
    """The workspace's preferences, each with its topics."""

    results: List[WorkspacePreferenceGetResponse]
