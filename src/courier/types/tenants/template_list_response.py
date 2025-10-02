# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TemplateListResponse", "Item", "ItemData"]


class ItemData(BaseModel):
    routing: "MessageRouting"


class Item(BaseModel):
    id: str
    """The template's id"""

    created_at: str
    """The timestamp at which the template was created"""

    data: ItemData
    """The template's data containing it's routing configs"""

    published_at: str
    """The timestamp at which the template was published"""

    updated_at: str
    """The timestamp at which the template was last updated"""

    version: str
    """The version of the template"""


class TemplateListResponse(BaseModel):
    has_more: bool
    """Set to true when there are more pages that can be retrieved."""

    type: Literal["list"]
    """Always set to `list`. Represents the type of this object."""

    url: str
    """A url that may be used to generate these results."""

    cursor: Optional[str] = None
    """A pointer to the next page of results.

    Defined only when `has_more` is set to true
    """

    items: Optional[List[Item]] = None

    next_url: Optional[str] = None
    """A url that may be used to generate fetch the next set of results.

    Defined only when `has_more` is set to true
    """


from ..message_routing import MessageRouting
