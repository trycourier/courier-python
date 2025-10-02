# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["List"]


class List(BaseModel):
    id: str

    name: str

    created: Optional[str] = None

    updated: Optional[str] = None
