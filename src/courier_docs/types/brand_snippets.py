# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrandSnippets", "Item"]


class Item(BaseModel):
    format: Literal["handlebars"]

    name: str

    value: str


class BrandSnippets(BaseModel):
    items: List[Item]
