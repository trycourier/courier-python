# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .preview_run import PreviewRun
from ...shared.paging import Paging

__all__ = ["PreviewRunListResponse"]


class PreviewRunListResponse(BaseModel):
    """Paginated list of preview runs, newest first."""

    paging: Paging

    results: List[PreviewRun]
