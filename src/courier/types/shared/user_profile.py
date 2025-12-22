# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .expo import Expo
from .slack import Slack
from .discord import Discord
from .intercom import Intercom
from .ms_teams import MsTeams
from ..._models import BaseModel
from .airship_profile import AirshipProfile
from .user_profile_firebase_token import UserProfileFirebaseToken

__all__ = ["UserProfile", "Address"]


class Address(BaseModel):
    country: str

    formatted: str

    locality: str

    postal_code: str

    region: str

    street_address: str


class UserProfile(BaseModel):
    address: Optional[Address] = None

    airship: Optional[AirshipProfile] = None

    apn: Optional[str] = None

    birthdate: Optional[str] = None

    custom: Optional[Dict[str, object]] = None
    """A free form object.

    Due to a limitation of the API Explorer, you can only enter string key/values
    below, but this API accepts more complex object structures.
    """

    discord: Optional[Discord] = None

    email: Optional[str] = None

    email_verified: Optional[bool] = None

    expo: Optional[Expo] = None

    facebook_psid: Optional[str] = FieldInfo(alias="facebookPSID", default=None)

    family_name: Optional[str] = None

    firebase_token: Optional[UserProfileFirebaseToken] = FieldInfo(alias="firebaseToken", default=None)

    gender: Optional[str] = None

    given_name: Optional[str] = None

    intercom: Optional[Intercom] = None

    locale: Optional[str] = None

    middle_name: Optional[str] = None

    ms_teams: Optional[MsTeams] = None

    name: Optional[str] = None

    nickname: Optional[str] = None

    phone_number: Optional[str] = None

    phone_number_verified: Optional[bool] = None

    picture: Optional[str] = None

    preferred_name: Optional[str] = None

    profile: Optional[str] = None

    slack: Optional[Slack] = None

    sub: Optional[str] = None

    target_arn: Optional[str] = None

    updated_at: Optional[str] = None

    website: Optional[str] = None

    zoneinfo: Optional[str] = None
