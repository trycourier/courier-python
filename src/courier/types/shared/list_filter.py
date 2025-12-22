# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ListFilter"]


class ListFilter(BaseModel):
    operator: Literal["MEMBER_OF"]
    """Send to users only if they are member of the account"""

    path: Literal["account_id"]

    value: str
