# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .digest_instance import DigestInstance

__all__ = ["DigestInstanceListResponse"]


class DigestInstanceListResponse(BaseModel):
    has_more: bool
    """Whether there are more digest instances to fetch using the cursor."""

    items: List[DigestInstance]
    """The digest instances for this page of results."""

    type: Literal["list"]
    """Always `list` for a paginated list response."""

    cursor: Optional[str] = None
    """
    A cursor token for fetching the next page of results, or null when there are
    none.
    """

    next_url: Optional[str] = None
    """The path to fetch the next page of results, or null when there are none."""

    url: Optional[str] = None
    """The path of the current request."""
