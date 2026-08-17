# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .token import Token
from .multiple_tokens import MultipleTokens

__all__ = ["Apn"]

Apn: TypeAlias = Union[Token, MultipleTokens]
