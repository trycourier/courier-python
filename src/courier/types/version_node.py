# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VersionNode"]


class VersionNode(BaseModel):
    """A version entry for a notification template."""

    created: int
    """Epoch milliseconds when this version was created."""

    creator: str
    """User ID of the version creator."""

    version: str
    """Version identifier.

    One of "draft", "published:vNNN" (current published version), or "vNNN"
    (historical version).
    """

    has_changes: Optional[bool] = None
    """Whether the draft has unpublished changes. Only present on the draft version."""
