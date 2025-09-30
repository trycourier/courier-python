# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .default_preferences_param import DefaultPreferencesParam

__all__ = ["TenantUpdateParams"]


class TenantUpdateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the tenant."""

    brand_id: Optional[str]
    """Brand to be used for the account when one is not specified by the send call."""

    default_preferences: Optional[DefaultPreferencesParam]
    """
    Defines the preferences used for the tenant when the user hasn't specified their
    own.
    """

    parent_tenant_id: Optional[str]
    """Tenant's parent id (if any)."""

    properties: Optional[Dict[str, object]]
    """Arbitrary properties accessible to a template."""

    user_profile: Optional[Dict[str, object]]
    """A user profile object merged with user profile on send."""
