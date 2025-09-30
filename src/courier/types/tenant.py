# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .default_preferences import DefaultPreferences

__all__ = ["Tenant"]


class Tenant(BaseModel):
    id: str
    """Id of the tenant."""

    name: str
    """Name of the tenant."""

    brand_id: Optional[str] = None
    """Brand to be used for the account when one is not specified by the send call."""

    default_preferences: Optional[DefaultPreferences] = None
    """
    Defines the preferences used for the account when the user hasn't specified
    their own.
    """

    parent_tenant_id: Optional[str] = None
    """Tenant's parent id (if any)."""

    properties: Optional[Dict[str, object]] = None
    """Arbitrary properties accessible to a template."""

    user_profile: Optional[Dict[str, object]] = None
    """A user profile object merged with user profile on send."""
