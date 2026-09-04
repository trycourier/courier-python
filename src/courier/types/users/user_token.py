# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UserToken", "Device", "Tracking"]


class Device(BaseModel):
    """Information about the device the token came from."""

    ad_id: Optional[str] = None
    """Id of the advertising identifier"""

    app_id: Optional[str] = None
    """Id of the application the token is used for"""

    device_id: Optional[str] = None
    """Id of the device the token is associated with"""

    manufacturer: Optional[str] = None
    """The device manufacturer"""

    model: Optional[str] = None
    """The device model"""

    platform: Optional[str] = None
    """The device platform i.e. android, ios, web"""


class Tracking(BaseModel):
    """Tracking information about the device the token came from."""

    ip: Optional[str] = None
    """The IP address of the device"""

    lat: Optional[str] = None
    """The latitude of the device"""

    long: Optional[str] = None
    """The longitude of the device"""

    os_version: Optional[str] = None
    """The operating system version"""


class UserToken(BaseModel):
    token: str
    """Full body of the token. Must match token in URL path parameter."""

    provider_key: Literal["firebase-fcm", "apn", "expo", "onesignal"]

    device: Optional[Device] = None
    """Information about the device the token came from."""

    expiry_date: Union[str, bool, None] = None
    """When the token expires.

    Accepts a date, or the boolean `false` to disable expiration entirely. ISO 8601
    is recommended (for example `2026-10-25T00:00:00.000Z`). A value that cannot be
    parsed as a date is rejected; it is not treated as "no expiration" and does not
    fall back to the default. `true` is not a supported value. Omit the field to use
    the default, which expires a token that has not been re-registered for 60 days.
    """

    properties: Optional[object] = None
    """Properties about the token."""

    tracking: Optional[Tracking] = None
    """Tracking information about the device the token came from."""
