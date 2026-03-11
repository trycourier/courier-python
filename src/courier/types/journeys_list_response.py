# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .journey import Journey
from .._models import BaseModel

__all__ = ["JourneysListResponse"]


class JourneysListResponse(BaseModel):
    cursor: Optional[str] = None
    """A cursor token for pagination. Present when there are more results available."""

    templates: Optional[List[Journey]] = None
