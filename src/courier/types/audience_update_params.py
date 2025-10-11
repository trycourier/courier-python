# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.filter import Filter

__all__ = ["AudienceUpdateParams"]


class AudienceUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """A description of the audience"""

    filter: Optional[Filter]
    """A single filter to use for filtering"""

    name: Optional[str]
    """The name of the audience"""
