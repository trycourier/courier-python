# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .preference_section_get_response import PreferenceSectionGetResponse

__all__ = ["PreferenceSectionListResponse"]


class PreferenceSectionListResponse(BaseModel):
    """The workspace's preference sections, each with its topics."""

    results: List[PreferenceSectionGetResponse]
