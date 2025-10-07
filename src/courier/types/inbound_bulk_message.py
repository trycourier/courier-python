# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from .content import Content
from .._models import BaseModel

__all__ = ["InboundBulkMessage", "InboundBulkTemplateMessage", "InboundBulkContentMessage"]


class InboundBulkTemplateMessage(BaseModel):
    template: str

    brand: Optional[str] = None

    data: Optional[Dict[str, object]] = None

    event: Optional[str] = None

    locale: Optional[Dict[str, Dict[str, object]]] = None

    override: Optional[Dict[str, object]] = None


class InboundBulkContentMessage(BaseModel):
    content: Content
    """Syntactic sugar to provide a fast shorthand for Courier Elemental Blocks."""

    brand: Optional[str] = None

    data: Optional[Dict[str, object]] = None

    event: Optional[str] = None

    locale: Optional[Dict[str, Dict[str, object]]] = None

    override: Optional[Dict[str, object]] = None


InboundBulkMessage: TypeAlias = Union[InboundBulkTemplateMessage, InboundBulkContentMessage]
