# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .bulk_preference_topic import BulkPreferenceTopic

__all__ = ["PreferenceBulkUpdateResponse", "Error"]


class Error(BaseModel):
    """A single topic that could not be applied in a bulk preference request."""

    reason: str
    """A human-readable explanation of why the topic could not be applied."""

    topic_id: str


class PreferenceBulkUpdateResponse(BaseModel):
    errors: List[Error]
    """The topics that could not be applied, each with a reason."""

    items: List[BulkPreferenceTopic]
    """The topics that were successfully created or updated."""
