# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["JourneyVersionItem"]


class JourneyVersionItem(BaseModel):
    """A published version of a journey."""

    created: Optional[int] = None

    creator: Optional[str] = None

    name: str

    published: Optional[int] = None

    version: str
