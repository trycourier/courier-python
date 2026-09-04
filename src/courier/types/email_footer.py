# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EmailFooter",
    "Social",
    "SocialFacebook",
    "SocialInstagram",
    "SocialLinkedin",
    "SocialMedium",
    "SocialTwitter",
]


class SocialFacebook(BaseModel):
    url: Optional[str] = None


class SocialInstagram(BaseModel):
    url: Optional[str] = None


class SocialLinkedin(BaseModel):
    url: Optional[str] = None


class SocialMedium(BaseModel):
    url: Optional[str] = None


class SocialTwitter(BaseModel):
    url: Optional[str] = None


class Social(BaseModel):
    """Social links rendered in the email footer."""

    facebook: Optional[SocialFacebook] = None

    instagram: Optional[SocialInstagram] = None

    linkedin: Optional[SocialLinkedin] = None

    medium: Optional[SocialMedium] = None

    twitter: Optional[SocialTwitter] = None


class EmailFooter(BaseModel):
    inherit_default: Optional[bool] = FieldInfo(alias="inheritDefault", default=None)

    markdown: Optional[str] = None
    """The footer body, as markdown.

    This is the field the API returns and accepts; it is omitted entirely when no
    footer body is set. Sending null is accepted and treated as no footer body.
    """

    social: Optional[Social] = None
    """Social links rendered in the email footer."""
