# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .device_type import DeviceType
from .airship_profile_audience import AirshipProfileAudience

__all__ = ["AirshipProfile"]


class AirshipProfile(BaseModel):
    audience: AirshipProfileAudience

    device_types: List[DeviceType]
