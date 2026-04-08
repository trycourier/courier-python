# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .notification_template_state import NotificationTemplateState

__all__ = ["NotificationContentMutationResponse", "Element"]


class Element(BaseModel):
    id: str

    checksum: str


class NotificationContentMutationResponse(BaseModel):
    """
    Shared mutation response for `PUT` content, `PUT` element, and `PUT` locale operations. Contains the template ID, content version, per-element checksums, and resulting state.
    """

    id: str
    """Template ID."""

    elements: List[Element]

    state: NotificationTemplateState
    """Template state. Defaults to `DRAFT`."""

    version: str
    """Content version identifier."""
