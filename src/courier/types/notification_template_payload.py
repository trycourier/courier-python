# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.elemental_content import ElementalContent

__all__ = ["NotificationTemplatePayload", "Brand", "Routing", "Subscription"]


class Brand(BaseModel):
    """Brand reference, or null for no brand."""

    id: str


class Routing(BaseModel):
    """Routing strategy reference, or null for none."""

    strategy_id: str


class Subscription(BaseModel):
    """Subscription topic reference, or null for none."""

    topic_id: str


class NotificationTemplatePayload(BaseModel):
    """
    Full document shape used in POST and PUT request bodies, and returned inside the GET response envelope.
    """

    brand: Optional[Brand] = None
    """Brand reference, or null for no brand."""

    content: ElementalContent
    """Elemental content definition."""

    name: str
    """Display name for the template."""

    routing: Optional[Routing] = None
    """Routing strategy reference, or null for none."""

    subscription: Optional[Subscription] = None
    """Subscription topic reference, or null for none."""

    tags: List[str]
    """Tags for categorization. Send empty array for none."""
