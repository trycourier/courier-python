# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .preview_device import PreviewDevice

__all__ = ["PreviewDeviceListResponse"]


class PreviewDeviceListResponse(BaseModel):
    """The full catalog of renderable devices. Not paginated."""

    results: List[PreviewDevice]
