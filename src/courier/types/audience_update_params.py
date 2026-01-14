# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AudienceUpdateParams"]


class AudienceUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """A description of the audience"""

    filter: Optional["AudienceFilterConfig"]
    """
    Filter configuration for audience membership containing an array of filter rules
    """

    name: Optional[str]
    """The name of the audience"""

    operator: Optional[Literal["AND", "OR"]]
    """The logical operator (AND/OR) for the top-level filter"""


from .shared_params.audience_filter_config import AudienceFilterConfig
