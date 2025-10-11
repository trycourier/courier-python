# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .brand_snippet import BrandSnippet

__all__ = ["BrandSnippets"]


class BrandSnippets(TypedDict, total=False):
    items: Optional[Iterable[BrandSnippet]]
