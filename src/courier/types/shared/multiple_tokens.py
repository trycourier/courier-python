# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .token import Token
from ..._models import BaseModel

__all__ = ["MultipleTokens"]


class MultipleTokens(BaseModel):
    tokens: List[Token]
