# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

__all__ = ["BrandColorsParam"]


class BrandColorsParamTyped(TypedDict, total=False):
    primary: Optional[str]

    secondary: Optional[str]


BrandColorsParam: TypeAlias = Union[BrandColorsParamTyped, Dict[str, str]]
