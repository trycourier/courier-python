# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrandSnippet"]


class BrandSnippet(BaseModel):
    format: Literal["handlebars"]

    name: str

    value: str
