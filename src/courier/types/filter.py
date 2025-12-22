# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .single_filter_config import SingleFilterConfig

__all__ = ["Filter"]

Filter: TypeAlias = Union[SingleFilterConfig, "NestedFilterConfig"]

from .nested_filter_config import NestedFilterConfig
