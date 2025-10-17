# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .user_token import UserToken

__all__ = ["TokenRetrieveResponse"]


class TokenRetrieveResponse(UserToken):
    status: Optional[Literal["active", "unknown", "failed", "revoked"]] = None

    status_reason: Optional[str] = None
    """The reason for the token status."""
