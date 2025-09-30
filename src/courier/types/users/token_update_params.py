# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TokenUpdateParams", "Patch"]


class TokenUpdateParams(TypedDict, total=False):
    user_id: Required[str]

    patch: Required[Iterable[Patch]]


class Patch(TypedDict, total=False):
    op: Required[str]
    """The operation to perform."""

    path: Required[str]
    """The JSON path specifying the part of the profile to operate on."""

    value: Optional[str]
    """The value for the operation."""
