# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import TypeAlias, TypedDict

__all__ = ["BrandColors"]


class BrandColorsTyped(TypedDict, total=False):
    primary: str

    secondary: str


BrandColors: TypeAlias = Union[BrandColorsTyped, Dict[str, str]]
