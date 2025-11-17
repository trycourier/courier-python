# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthIssueTokenParams"]


class AuthIssueTokenParams(TypedDict, total=False):
    expires_in: Required[str]
    """Duration for token expiration.

    Accepts various time formats: - "2 hours" - 2 hours from now - "1d" - 1 day -
    "10h" - 10 hours - "2.5 hrs" - 2.5 hours - "1m" - 1 minute - "5s" - 5 seconds -
    "1y" - 1 year
    """

    scope: Required[str]
    """Space-separated list of scopes that define what the token can access.

    Common scopes include: Inbox Auth: - user_id:<user-id> - Access to a specific
    user (multiple can be listed) - read:messages - Read messages (requires user_id
    scope) - inbox:read:messages - Read inbox messages - inbox:write:events - Write
    inbox events (mark as read, etc.) Preferences Auth: - read:preferences - Read
    user preferences - write:preferences - Write user preferences Brands Auth: -
    read:brands[:<brand_id>] - Read brands (optionally specific brand) -
    write:brands[:<brand_id>] - Write brands (optionally specific brand) Example:
    "user_id:user123 inbox:read:messages inbox:write:events"
    """
