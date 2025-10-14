# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BaseCheck"]


class BaseCheck(BaseModel):
    id: str

    status: Literal["RESOLVED", "FAILED", "PENDING"]

    type: Literal["custom"]
