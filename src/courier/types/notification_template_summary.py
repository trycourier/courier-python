# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NotificationTemplateSummary"]


class NotificationTemplateSummary(BaseModel):
    """V2 (CDS) template summary returned in list responses."""

    id: str

    created: int
    """Epoch milliseconds when the template was created."""

    creator: str
    """User ID of the creator."""

    name: str

    state: Literal["DRAFT", "PUBLISHED"]

    tags: List[str]

    subscription_topic_id: Optional[str] = None
    """The linked subscription (preference) topic of the published version.

    Omitted when no topic is linked or the template has never been published.
    """

    updated: Optional[int] = None
    """Epoch milliseconds of last update."""

    updater: Optional[str] = None
    """User ID of the last updater."""
