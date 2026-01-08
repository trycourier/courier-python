# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AutomationTemplate"]


class AutomationTemplate(BaseModel):
    id: str
    """The unique identifier of the automation template."""

    name: str
    """The name of the automation template."""

    version: Literal["published", "draft"]
    """The version of the template published, draft."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """ISO 8601 timestamp when the template was created."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """ISO 8601 timestamp when the template was last updated."""
