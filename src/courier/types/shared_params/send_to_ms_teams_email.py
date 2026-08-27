# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SendToMsTeamsEmail"]


class SendToMsTeamsEmail(TypedDict, total=False):
    """Provide at least one of `tenant_id` or `service_url`.

    If you provide both, they must agree.
    """

    email: Required[str]

    service_url: str

    tenant_id: str
