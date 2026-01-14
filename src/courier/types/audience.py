# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Audience"]


class Audience(BaseModel):
    id: str
    """A unique identifier representing the audience_id"""

    created_at: str

    description: str
    """A description of the audience"""

    name: str
    """The name of the audience"""

    updated_at: str

    filter: Optional["AudienceFilterConfig"] = None
    """
    Filter configuration for audience membership containing an array of filter rules
    """

    operator: Optional[Literal["AND", "OR"]] = None
    """The logical operator (AND/OR) for the top-level filter"""


from .shared.audience_filter_config import AudienceFilterConfig
