# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .notification_template_payload import NotificationTemplatePayload

__all__ = ["NotificationTemplateResponse", "Notification"]


class Notification(NotificationTemplatePayload):
    """
    Full document shape used in POST and PUT request bodies, and returned inside the GET response envelope.
    """

    id: str
    """The template ID."""


class NotificationTemplateResponse(BaseModel):
    """
    Response for GET /notifications/{id}, POST /notifications, and PUT /notifications/{id}. Wraps the template payload inside a `notification` key alongside metadata.
    """

    created: int
    """Epoch milliseconds when the template was created."""

    creator: str
    """User ID of the creator."""

    notification: Notification
    """
    Full document shape used in POST and PUT request bodies, and returned inside the
    GET response envelope.
    """

    state: Literal["DRAFT", "PUBLISHED"]
    """The template state. Always uppercase."""

    updated: Optional[int] = None
    """Epoch milliseconds of last update."""

    updater: Optional[str] = None
    """User ID of the last updater."""
