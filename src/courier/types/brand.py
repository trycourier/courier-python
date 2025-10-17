# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .brand_settings import BrandSettings
from .brand_snippets import BrandSnippets

__all__ = ["Brand"]


class Brand(BaseModel):
    id: str

    created: int

    name: str

    updated: int

    published: Optional[int] = None

    settings: Optional[BrandSettings] = None

    snippets: Optional[BrandSnippets] = None

    version: Optional[str] = None
