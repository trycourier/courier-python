# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .brand_settings import BrandSettings
from .brand_snippets import BrandSnippets

__all__ = ["Brand"]


class Brand(BaseModel):
    created: int
    """The date/time of when the brand was created.

    Represented in milliseconds since Unix epoch.
    """

    name: str
    """Brand name"""

    published: int
    """The date/time of when the brand was published.

    Represented in milliseconds since Unix epoch.
    """

    settings: BrandSettings

    updated: int
    """The date/time of when the brand was updated.

    Represented in milliseconds since Unix epoch.
    """

    version: str
    """The version identifier for the brand"""

    id: Optional[str] = None
    """Brand Identifier"""

    snippets: Optional[BrandSnippets] = None
