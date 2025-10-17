# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.elemental_content import ElementalContent
from .shared.elemental_content_sugar import ElementalContentSugar

__all__ = [
    "InboundBulkMessage",
    "InboundBulkTemplateMessage",
    "InboundBulkContentMessage",
    "InboundBulkContentMessageContent",
]


class InboundBulkTemplateMessage(BaseModel):
    template: str

    brand: Optional[str] = None

    data: Optional[Dict[str, object]] = None

    event: Optional[str] = None

    locale: Optional[Dict[str, Dict[str, object]]] = None

    override: Optional[Dict[str, object]] = None


InboundBulkContentMessageContent: TypeAlias = Union[ElementalContentSugar, ElementalContent]


class InboundBulkContentMessage(BaseModel):
    content: InboundBulkContentMessageContent
    """Syntactic sugar to provide a fast shorthand for Courier Elemental Blocks."""

    brand: Optional[str] = None

    data: Optional[Dict[str, object]] = None

    event: Optional[str] = None

    locale: Optional[Dict[str, Dict[str, object]]] = None

    override: Optional[Dict[str, object]] = None


InboundBulkMessage: TypeAlias = Union[InboundBulkTemplateMessage, InboundBulkContentMessage]
