# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AuthIssueTokenParams"]


class AuthIssueTokenParams(TypedDict, total=False):
    expires_in: Required[str]

    scope: Required[
        Literal[
            "read:preferences",
            "write:preferences",
            "read:user-tokens",
            "write:user-tokens",
            "read:brands",
            "write:brands",
            "read:brands{:id}",
            "write:brands{:id}",
            "write:track",
            "inbox:read:messages",
            "inbox:write:messages",
            "inbox:write:event",
            "inbox:write:events",
            "user_id:$YOUR_USER_ID",
        ]
    ]
