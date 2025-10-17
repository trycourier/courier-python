# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BaseTemplateTenantAssociation"]


class BaseTemplateTenantAssociation(BaseModel):
    id: str
    """The template's id"""

    created_at: str
    """The timestamp at which the template was created"""

    published_at: str
    """The timestamp at which the template was published"""

    updated_at: str
    """The timestamp at which the template was last updated"""

    version: str
    """The version of the template"""
