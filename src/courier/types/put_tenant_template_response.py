# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PutTenantTemplateResponse"]


class PutTenantTemplateResponse(BaseModel):
    """Response from creating or updating a tenant notification template"""

    id: str
    """The template ID"""

    version: str
    """The version of the saved template"""

    published_at: Optional[str] = None
    """The timestamp when the template was published.

    Only present if the template was published as part of this request.
    """
