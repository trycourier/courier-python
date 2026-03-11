# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Journey"]


class Journey(BaseModel):
    """A journey template representing an automation workflow."""

    id: str
    """The unique identifier of the journey."""

    name: str
    """The name of the journey."""

    version: Literal["published", "draft"]
    """The version of the journey (published or draft)."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """ISO 8601 timestamp when the journey was created."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """ISO 8601 timestamp when the journey was last updated."""
