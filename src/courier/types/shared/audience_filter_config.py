# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AudienceFilterConfig"]


class AudienceFilterConfig(BaseModel):
    """
    Filter configuration for audience membership containing an array of filter rules
    """

    filters: List["FilterConfig"]
    """Array of filter rules (single conditions or nested groups)"""

    operator: Optional[Literal["AND", "OR"]] = None
    """The logical operator (AND/OR) combining the rules in `filters`.

    Required when `filters` contains more than one rule. If omitted, the top-level
    `operator` field on the request is used instead.
    """


from .filter_config import FilterConfig
