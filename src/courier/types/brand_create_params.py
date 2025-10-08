# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared_params.brand_settings import BrandSettings
from .shared_params.brand_snippets import BrandSnippets

__all__ = ["BrandCreateParams"]


class BrandCreateParams(TypedDict, total=False):
    name: Required[str]

    id: Optional[str]

    settings: Optional[BrandSettings]

    snippets: Optional[BrandSnippets]
