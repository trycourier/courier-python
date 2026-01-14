# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel

__all__ = ["AudienceFilterConfig"]


class AudienceFilterConfig(BaseModel):
    """
    Filter configuration for audience membership containing an array of filter rules
    """

    filters: List["FilterConfig"]
    """Array of filter rules (single conditions or nested groups)"""


from .filter_config import FilterConfig
