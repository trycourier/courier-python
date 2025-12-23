# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .single_filter_config_param import SingleFilterConfigParam

__all__ = ["FilterParam"]

FilterParam: TypeAlias = Union[SingleFilterConfigParam, "NestedFilterConfigParam"]

from .nested_filter_config_param import NestedFilterConfigParam
