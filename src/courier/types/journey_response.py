# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .journey_state import JourneyState

__all__ = ["JourneyResponse"]


class JourneyResponse(BaseModel):
    """A journey, with its current draft or published nodes and metadata."""

    id: str

    created: Optional[int] = None

    creator: Optional[str] = None

    enabled: bool

    name: str

    nodes: List["JourneyNode"]

    published: Optional[int] = None

    state: JourneyState
    """Lifecycle state of a journey."""

    updated: Optional[int] = None

    updater: Optional[str] = None


from .journey_node import JourneyNode
