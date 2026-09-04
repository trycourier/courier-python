# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
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

    value: Union[str, bool, Dict[str, object], None]
    """The value for the operation.

    A string for most fields; boolean `false` when disabling token expiration via
    `expiry_date`, which cannot be expressed as a string.
    """
