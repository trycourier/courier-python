# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.elemental_content import ElementalContent
from .shared_params.elemental_content_sugar import ElementalContentSugar

__all__ = [
    "InboundBulkMessageParam",
    "InboundBulkTemplateMessage",
    "InboundBulkContentMessage",
    "InboundBulkContentMessageContent",
]


class InboundBulkTemplateMessage(TypedDict, total=False):
    template: Required[str]

    brand: Optional[str]

    data: Optional[Dict[str, object]]

    event: Optional[str]

    locale: Optional[Dict[str, Dict[str, object]]]

    override: Optional[Dict[str, object]]


InboundBulkContentMessageContent: TypeAlias = Union[ElementalContentSugar, ElementalContent]


class InboundBulkContentMessage(TypedDict, total=False):
    content: Required[InboundBulkContentMessageContent]
    """Syntactic sugar to provide a fast shorthand for Courier Elemental Blocks."""

    brand: Optional[str]

    data: Optional[Dict[str, object]]

    event: Optional[str]

    locale: Optional[Dict[str, Dict[str, object]]]

    override: Optional[Dict[str, object]]


InboundBulkMessageParam: TypeAlias = Union[InboundBulkTemplateMessage, InboundBulkContentMessage]
