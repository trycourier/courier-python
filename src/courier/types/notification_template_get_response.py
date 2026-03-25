# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .notification_template_payload import NotificationTemplatePayload

__all__ = ["NotificationTemplateGetResponse", "Notification"]


class Notification(NotificationTemplatePayload):
    """
    Full document shape used in POST and PUT request bodies, and returned inside the GET response envelope.
    """

    id: str
    """The template ID."""


class NotificationTemplateGetResponse(BaseModel):
    """Envelope response for GET /notifications/{id}.

    The notification object mirrors the POST/PUT input shape. Nullable fields return null when unset.
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
