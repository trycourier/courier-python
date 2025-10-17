# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .user_token import UserToken

__all__ = ["TokenListResponse"]

TokenListResponse: TypeAlias = List[UserToken]
