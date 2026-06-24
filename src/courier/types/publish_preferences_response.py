# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PublishPreferencesResponse"]


class PublishPreferencesResponse(BaseModel):
    """Result of publishing the workspace's preferences page."""

    page_id: str
    """Id of the published page snapshot."""

    published_at: str
    """ISO-8601 timestamp of the publish."""

    published_version: float
    """Monotonic published version (epoch milliseconds)."""

    preview_url: Optional[str] = None
    """Draft-mode hosted preferences page URL for previewing."""

    published_by: Optional[str] = None
    """Id of the publisher."""
