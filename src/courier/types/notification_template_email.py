# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NotificationTemplateEmail"]


class NotificationTemplateEmail(BaseModel):
    """
    Email header fields for the template's email channel: the From, Reply-to, CC and BCC values set in the Studio email channel settings. Each value may use template variables, such as `{{data.cc}}`, which are resolved at send time.
    Reads omit `email` when no header is set, and omit each unset field.
    Writes treat it as optional, with three meanings. Omit it to keep the stored headers. Send null to clear all four. Send an object to replace all four: a field the object leaves out is cleared. Other email channel settings, such as the subject, are kept either way. Headers only apply while `content` has an email channel; with no email channel they are not stored.
    """

    bcc: Optional[List[str]] = None
    """BCC addresses."""

    cc: Optional[List[str]] = None
    """CC addresses."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The From address."""

    reply_to: Optional[str] = None
    """The Reply-to address."""
