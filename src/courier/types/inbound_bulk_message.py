# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .tenants.elemental_content import ElementalContent

__all__ = [
    "InboundBulkMessage",
    "InboundBulkTemplateMessage",
    "InboundBulkContentMessage",
    "InboundBulkContentMessageContent",
    "InboundBulkContentMessageContentElementalContentSugar",
]


class InboundBulkTemplateMessage(BaseModel):
    template: str

    brand: Optional[str] = None

    data: Optional[Dict[str, object]] = None

    event: Optional[str] = None

    locale: Optional[Dict[str, Dict[str, object]]] = None

    override: Optional[Dict[str, object]] = None


class InboundBulkContentMessageContentElementalContentSugar(BaseModel):
    body: str
    """The text content displayed in the notification."""

    title: str
    """Title/subject displayed by supported channels."""


InboundBulkContentMessageContent: TypeAlias = Union[
    InboundBulkContentMessageContentElementalContentSugar, ElementalContent
]


class InboundBulkContentMessage(BaseModel):
    content: InboundBulkContentMessageContent
    """Syntactic sugar to provide a fast shorthand for Courier Elemental Blocks."""

    brand: Optional[str] = None

    data: Optional[Dict[str, object]] = None

    event: Optional[str] = None

    locale: Optional[Dict[str, Dict[str, object]]] = None

    override: Optional[Dict[str, object]] = None


InboundBulkMessage: TypeAlias = Union[InboundBulkTemplateMessage, InboundBulkContentMessage]
