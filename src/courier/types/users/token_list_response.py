# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .user_token import UserToken

__all__ = ["TokenListResponse"]


class TokenListResponse(BaseModel):
    tokens: List[UserToken]
