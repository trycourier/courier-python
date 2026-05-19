# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["JourneyTemplateSummary"]


class JourneyTemplateSummary(BaseModel):
    """
    Summary fields of a journey-scoped notification template returned in list responses.
    """

    id: str

    created: int

    creator: str

    name: str

    state: str

    tags: List[str]

    updated: Optional[int] = None

    updater: Optional[str] = None
