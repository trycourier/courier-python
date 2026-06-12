# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .digest_category import DigestCategory

__all__ = ["DigestInstance"]


class DigestInstance(BaseModel):
    digest_instance_id: str
    """A unique identifier for the digest instance."""

    event_count: int
    """The total number of events received for this instance."""

    status: Literal["IN_PROGRESS", "COMPLETED"]
    """The status of the digest instance.

    `IN_PROGRESS` instances are still accumulating events; `COMPLETED` instances
    have been released.
    """

    user_id: str
    """The ID of the user this digest instance belongs to."""

    categories: Optional[List[DigestCategory]] = None
    """The categories configured for the digest."""

    category_key_counts: Optional[Dict[str, int]] = None
    """A map of category key to the number of events received for that category."""

    created_at: Optional[str] = None
    """An ISO 8601 timestamp of when the digest instance was created."""

    disabled: Optional[bool] = None
    """Whether the digest instance has been disabled."""

    tenant_id: Optional[str] = None
    """The ID of the tenant this digest instance belongs to, if any."""
