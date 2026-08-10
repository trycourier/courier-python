# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .notification_template_alias import NotificationTemplateAlias
from .notification_template_payload import NotificationTemplatePayload

__all__ = ["NotificationTemplateResponse"]


class NotificationTemplateResponse(NotificationTemplatePayload):
    """
    Response for GET /notifications/{id}, POST /notifications, and PUT /notifications/{id}. Returns all template fields at the top level.
    """

    id: str
    """The template ID."""

    created: int
    """Epoch milliseconds when the template was created."""

    creator: str
    """User ID of the creator."""

    state: Literal["DRAFT", "PUBLISHED"]
    """The template state. Always uppercase."""

    alias: Optional[NotificationTemplateAlias] = None
    """
    A template's send-time alias as returned by a read, omitted entirely when it has
    none. Usually a single string; an array for a template that resolves from
    several aliases, which writes through this API can no longer produce — only
    templates predating that restriction, or aliases attached outside this API, hold
    more than one.
    """

    updated: Optional[int] = None
    """Epoch milliseconds of last update."""

    updater: Optional[str] = None
    """User ID of the last updater."""
