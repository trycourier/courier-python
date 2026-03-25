# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NotificationTemplateMutationResponse", "Notification"]


class Notification(BaseModel):
    id: str
    """The ID of the created or updated template."""


class NotificationTemplateMutationResponse(BaseModel):
    """Response returned by POST and PUT operations."""

    notification: Notification

    state: Literal["DRAFT", "PUBLISHED"]
    """The template state after the operation. Always uppercase."""
