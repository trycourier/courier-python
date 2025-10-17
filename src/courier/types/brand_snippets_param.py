# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .brand_snippet_param import BrandSnippetParam

__all__ = ["BrandSnippetsParam"]


class BrandSnippetsParam(TypedDict, total=False):
    items: Optional[Iterable[BrandSnippetParam]]
