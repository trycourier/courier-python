# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .preference import Preference

__all__ = ["ProfilePreferences"]


class ProfilePreferences(TypedDict, total=False):
    notifications: Required[Dict[str, Preference]]

    categories: Optional[Dict[str, Preference]]

    template_id: Annotated[Optional[str], PropertyInfo(alias="templateId")]
