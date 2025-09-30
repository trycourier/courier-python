# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TenantAssociationParam"]


class TenantAssociationParam(TypedDict, total=False):
    tenant_id: Required[str]
    """Tenant ID for the association between tenant and user"""

    profile: Optional[Dict[str, object]]
    """
    Additional metadata to be applied to a user profile when used in a tenant
    context
    """

    type: Optional[Literal["user"]]

    user_id: Optional[str]
    """User ID for the association between tenant and user"""
