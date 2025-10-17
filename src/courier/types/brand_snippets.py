# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .brand_snippet import BrandSnippet

__all__ = ["BrandSnippets"]


class BrandSnippets(BaseModel):
    items: Optional[List[BrandSnippet]] = None
