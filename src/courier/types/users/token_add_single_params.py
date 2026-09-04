# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenAddSingleParams", "Device", "Tracking"]


class TokenAddSingleParams(TypedDict, total=False):
    user_id: Required[str]

    provider_key: Required[Literal["firebase-fcm", "apn", "expo", "onesignal"]]

    device: Optional[Device]
    """Information about the device the token came from."""

    expiry_date: Union[str, bool, None]
    """When the token expires.

    Accepts a date, or the boolean `false` to disable expiration entirely. ISO 8601
    is recommended (for example `2026-10-25T00:00:00.000Z`). A value that cannot be
    parsed as a date is rejected; it is not treated as "no expiration" and does not
    fall back to the default. `true` is not a supported value. Omit the field to use
    the default, which expires a token that has not been re-registered for 60 days.
    """

    properties: object
    """Properties about the token."""

    tracking: Optional[Tracking]
    """Tracking information about the device the token came from."""


class Device(TypedDict, total=False):
    """Information about the device the token came from."""

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
    """Tracking information about the device the token came from."""

    ip: Optional[str]
    """The IP address of the device"""

    lat: Optional[str]
    """The latitude of the device"""

    long: Optional[str]
    """The longitude of the device"""

    os_version: Optional[str]
    """The operating system version"""
