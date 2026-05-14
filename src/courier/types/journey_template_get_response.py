# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.elemental_node import ElementalNode

__all__ = ["JourneyTemplateGetResponse", "Brand", "Content", "Subscription"]


class Brand(BaseModel):
    id: str


class Content(BaseModel):
    elements: List[ElementalNode]

    version: Literal["2022-01-01"]

    scope: Optional[Literal["default", "strict"]] = None


class Subscription(BaseModel):
    topic_id: str


class JourneyTemplateGetResponse(BaseModel):
    id: str

    brand: Optional[Brand] = None

    content: Content

    created: int

    creator: str

    name: str

    state: Literal["DRAFT", "PUBLISHED"]

    subscription: Optional[Subscription] = None

    tags: List[str]

    updated: Optional[int] = None

    updater: Optional[str] = None
