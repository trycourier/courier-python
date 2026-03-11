# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["JourneyInvokeParams"]


class JourneyInvokeParams(TypedDict, total=False):
    data: Dict[str, object]
    """Data payload passed to the journey.

    The expected shape can be predefined using the schema builder in the journey
    editor. This data is available in journey steps for condition evaluation and
    template variable interpolation. Can also contain user identifiers (user_id,
    userId, anonymousId) if not provided elsewhere.
    """

    profile: Dict[str, object]
    """Profile data for the user.

    Can contain contact information (email, phone_number), user identifiers
    (user_id, userId, anonymousId), or any custom profile fields. Profile fields are
    merged with any existing stored profile for the user. Include context.tenant_id
    to load a tenant-scoped profile for multi-tenant scenarios.
    """

    user_id: str
    """A unique identifier for the user.

    If not provided, the system will attempt to resolve the user identifier from
    profile or data objects.
    """
