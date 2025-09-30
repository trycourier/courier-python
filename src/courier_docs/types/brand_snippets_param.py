# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrandSnippetsParam", "Item"]


class Item(TypedDict, total=False):
    format: Required[Literal["handlebars"]]

    name: Required[str]

    value: Required[str]


class BrandSnippetsParam(TypedDict, total=False):
    items: Required[Iterable[Item]]
