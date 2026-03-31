# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["MessageProvidersType"]


class MessageProvidersType(BaseModel):
    if_: Optional[str] = FieldInfo(alias="if", default=None)
    """JS conditional with access to data/profile."""

    metadata: Optional[Metadata] = None

    override: Optional[Dict[str, object]] = None
    """Provider-specific overrides."""

    timeouts: Optional[int] = None
