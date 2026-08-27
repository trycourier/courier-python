# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SendToMsTeamsUserID"]


class SendToMsTeamsUserID(TypedDict, total=False):
    """Provide at least one of `tenant_id` or `service_url`.

    If you provide both, they must agree.
    """

    user_id: Required[str]

    service_url: str

    tenant_id: str
