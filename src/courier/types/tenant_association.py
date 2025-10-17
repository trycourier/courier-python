# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TenantAssociation"]


class TenantAssociation(BaseModel):
    tenant_id: str
    """Tenant ID for the association between tenant and user"""

    profile: Optional[Dict[str, object]] = None
    """
    Additional metadata to be applied to a user profile when used in a tenant
    context
    """

    type: Optional[Literal["user"]] = None

    user_id: Optional[str] = None
    """User ID for the association between tenant and user"""
