# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UserToken", "Device", "Tracking"]


class Device(BaseModel):
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
    """ISO 8601 formatted date the token expires.

    Defaults to 2 months. Set to false to disable expiration.
    """

    properties: Optional[object] = None
    """Properties about the token."""

    tracking: Optional[Tracking] = None
    """Tracking information about the device the token came from."""
