# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["Filter"]


class Filter(BaseModel):
    """Filter that contains an array of FilterConfig items"""

    filters: List["FilterConfig"]


from .filter_config import FilterConfig
