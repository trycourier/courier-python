# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .brand_settings_param import BrandSettingsParam
from .brand_snippets_param import BrandSnippetsParam

__all__ = ["BrandCreateParams"]


class BrandCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the brand."""

    settings: Required[BrandSettingsParam]

    id: Optional[str]

    snippets: Optional[BrandSnippetsParam]
