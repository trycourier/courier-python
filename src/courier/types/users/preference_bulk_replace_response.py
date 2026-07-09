# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .bulk_preference_topic import BulkPreferenceTopic

__all__ = ["PreferenceBulkReplaceResponse"]


class PreferenceBulkReplaceResponse(BaseModel):
    deleted: List[str]
    """The ids of the overrides that were reset to their topic default."""

    items: List[BulkPreferenceTopic]
    """The complete resulting set of topic overrides for the user."""
