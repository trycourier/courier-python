# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EmailFooterParam",
    "Social",
    "SocialFacebook",
    "SocialInstagram",
    "SocialLinkedin",
    "SocialMedium",
    "SocialTwitter",
]


class SocialFacebook(TypedDict, total=False):
    url: Optional[str]


class SocialInstagram(TypedDict, total=False):
    url: Optional[str]


class SocialLinkedin(TypedDict, total=False):
    url: Optional[str]


class SocialMedium(TypedDict, total=False):
    url: Optional[str]


class SocialTwitter(TypedDict, total=False):
    url: Optional[str]


class Social(TypedDict, total=False):
    """Social links rendered in the email footer."""

    facebook: Optional[SocialFacebook]

    instagram: Optional[SocialInstagram]

    linkedin: Optional[SocialLinkedin]

    medium: Optional[SocialMedium]

    twitter: Optional[SocialTwitter]


class EmailFooterParam(TypedDict, total=False):
    inherit_default: Annotated[Optional[bool], PropertyInfo(alias="inheritDefault")]

    markdown: Optional[str]
    """The footer body, as markdown.

    This is the field the API returns and accepts; it is omitted entirely when no
    footer body is set. Sending null is accepted and treated as no footer body.
    """

    social: Optional[Social]
    """Social links rendered in the email footer."""
