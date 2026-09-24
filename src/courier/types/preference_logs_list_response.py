# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.paging import Paging
from .preference_change_log_entry import PreferenceChangeLogEntry

__all__ = ["PreferenceLogsListResponse"]


class PreferenceLogsListResponse(BaseModel):
    items: List[PreferenceChangeLogEntry]
    """One entry per preference change, newest first."""

    paging: Paging
