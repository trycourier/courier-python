# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PostTenantTemplatePublishResponse"]


class PostTenantTemplatePublishResponse(BaseModel):
    """Response from publishing a tenant template"""

    id: str
    """The template ID"""

    published_at: str
    """The timestamp when the template was published"""

    version: str
    """The published version of the template"""
