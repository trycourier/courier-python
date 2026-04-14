# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared_params.elemental_content import ElementalContent

__all__ = ["NotificationTemplatePayloadParam", "Brand", "Routing", "Subscription"]


class Brand(TypedDict, total=False):
    """Brand reference, or null for no brand."""

    id: Required[str]


class Routing(TypedDict, total=False):
    """Routing strategy reference, or null for none."""

    strategy_id: Required[str]


class Subscription(TypedDict, total=False):
    """Subscription topic reference, or null for none."""

    topic_id: Required[str]


class NotificationTemplatePayloadParam(TypedDict, total=False):
    """
    Core template fields used in POST and PUT request bodies (nested under a `notification` key) and returned at the top level in responses.
    """

    brand: Required[Optional[Brand]]
    """Brand reference, or null for no brand."""

    content: Required[ElementalContent]
    """Elemental content definition."""

    name: Required[str]
    """Display name for the template."""

    routing: Required[Optional[Routing]]
    """Routing strategy reference, or null for none."""

    subscription: Required[Optional[Subscription]]
    """Subscription topic reference, or null for none."""

    tags: Required[SequenceNotStr[str]]
    """Tags for categorization. Send empty array for none."""
