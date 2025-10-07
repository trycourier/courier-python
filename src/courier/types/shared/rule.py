# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Rule"]


class Rule(BaseModel):
    until: str

    start: Optional[str] = None
