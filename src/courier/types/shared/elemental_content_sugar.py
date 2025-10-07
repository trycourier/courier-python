# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ElementalContentSugar"]


class ElementalContentSugar(BaseModel):
    body: str
    """The text content displayed in the notification."""

    title: str
    """Title/subject displayed by supported channels."""
