# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["AudienceFilterConfig"]


class AudienceFilterConfig(TypedDict, total=False):
    """
    Filter configuration for audience membership containing an array of filter rules
    """

    filters: Required[Iterable["FilterConfig"]]
    """Array of filter rules (single conditions or nested groups)"""


from .filter_config import FilterConfig
