# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .device_set import DeviceSet

__all__ = ["DeviceSetListResponse"]


class DeviceSetListResponse(BaseModel):
    """The workspace's active device sets. Not paginated."""

    results: List[DeviceSet]
