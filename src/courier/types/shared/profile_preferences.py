# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .preference import Preference

__all__ = ["ProfilePreferences"]


class ProfilePreferences(BaseModel):
    notifications: Dict[str, Preference]

    categories: Optional[Dict[str, Preference]] = None

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)
