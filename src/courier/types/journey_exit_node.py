# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JourneyExitNode"]


class JourneyExitNode(BaseModel):
    """Terminate the journey run."""

    type: Literal["exit"]

    id: Optional[str] = None
