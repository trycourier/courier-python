# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["FilterParam"]


class FilterParam(TypedDict, total=False):
    """Filter that contains an array of FilterConfig items"""

    filters: Required[Iterable["FilterConfigParam"]]


from .filter_config_param import FilterConfigParam
