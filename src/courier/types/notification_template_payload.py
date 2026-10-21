# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.elemental_content import ElementalContent
from .notification_template_email import NotificationTemplateEmail

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
    Core template fields used in POST and PUT request bodies (nested under a `notification` key) and returned at the top level in responses.
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

    email: Optional[NotificationTemplateEmail] = None
    """
    Email header fields for the template's email channel: the From, Reply-to, CC and
    BCC values set in the Studio email channel settings. Each value may use template
    variables, such as `{{data.cc}}`, which are resolved at send time. Reads omit
    `email` when no header is set, and omit each unset field. Writes treat it as
    optional, with three meanings. Omit it to keep the stored headers. Send null to
    clear all four. Send an object to replace all four: a field the object leaves
    out is cleared. Other email channel settings, such as the subject, are kept
    either way. Headers only apply while `content` has an email channel; with no
    email channel they are not stored.
    """
