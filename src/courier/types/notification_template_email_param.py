# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["NotificationTemplateEmailParam"]

_NotificationTemplateEmailParamReservedKeywords = TypedDict(
    "_NotificationTemplateEmailParamReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class NotificationTemplateEmailParam(_NotificationTemplateEmailParamReservedKeywords, total=False):
    """
    Email header fields for the template's email channel: the From, Reply-to, CC and BCC values set in the Studio email channel settings. Each value may use template variables, such as `{{data.cc}}`, which are resolved at send time.
    Reads omit `email` when no header is set, and omit each unset field.
    Writes treat it as optional, with three meanings. Omit it to keep the stored headers. Send null to clear all four. Send an object to replace all four: a field the object leaves out is cleared. Other email channel settings, such as the subject, are kept either way. Headers only apply while `content` has an email channel; with no email channel they are not stored.
    """

    bcc: SequenceNotStr[str]
    """BCC addresses."""

    cc: SequenceNotStr[str]
    """CC addresses."""

    reply_to: str
    """The Reply-to address."""
