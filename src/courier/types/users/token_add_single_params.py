# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TokenAddSingleParams", "Device", "Tracking"]


class TokenAddSingleParams(TypedDict, total=False):
    user_id: Required[str]

    body_token: Required[Annotated[str, PropertyInfo(alias="token")]]
    """Full body of the token. Must match token in URL path parameter."""

    provider_key: Required[Literal["firebase-fcm", "apn", "expo", "onesignal"]]

    device: Optional[Device]
    """Information about the device the token came from."""

    expiry_date: Union[str, bool, None]
    """ISO 8601 formatted date the token expires.

    Defaults to 2 months. Set to false to disable expiration.
    """

    properties: object
    """Properties about the token."""

    tracking: Optional[Tracking]
    """Tracking information about the device the token came from."""


class Device(TypedDict, total=False):
    ad_id: Optional[str]
    """Id of the advertising identifier"""

    app_id: Optional[str]
    """Id of the application the token is used for"""

    device_id: Optional[str]
    """Id of the device the token is associated with"""

    manufacturer: Optional[str]
    """The device manufacturer"""

    model: Optional[str]
    """The device model"""

    platform: Optional[str]
    """The device platform i.e. android, ios, web"""


class Tracking(TypedDict, total=False):
    ip: Optional[str]
    """The IP address of the device"""

    lat: Optional[str]
    """The latitude of the device"""

    long: Optional[str]
    """The longitude of the device"""

    os_version: Optional[str]
    """The operating system version"""
