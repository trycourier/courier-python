# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TopicReleaseDigestParams"]


class TopicReleaseDigestParams(TypedDict, total=False):
    section_id: Required[str]

    user_id: Required[str]
    """The recipient whose digest to release.

    Required: there is no "release everyone on this topic" form, because a
    whole-schedule flush already has its own endpoint and a body-shaped difference
    between one recipient and all of them is too easy to get wrong.
    """

    tenant_id: str
    """
    The recipient's tenant, when they were sent to as part of one -- the same value
    returned as `tenant_id` on a digest instance and sent as
    `message.context.tenant_id`. It is part of the held digest's key, so a tenanted
    recipient cannot be found without it. Omit for an ordinary recipient.
    """
