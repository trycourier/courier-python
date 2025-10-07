# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["BrandSnippetsParam", "Item"]


class Item(TypedDict, total=False):
    name: Required[str]

    value: Required[str]


class BrandSnippetsParam(TypedDict, total=False):
    items: Optional[Iterable[Item]]
