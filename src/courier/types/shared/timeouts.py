# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Timeouts"]


class Timeouts(BaseModel):
    channel: Optional[int] = None

    provider: Optional[int] = None
