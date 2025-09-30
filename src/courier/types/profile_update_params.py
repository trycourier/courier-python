# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ProfileUpdateParams", "Patch"]


class ProfileUpdateParams(TypedDict, total=False):
    patch: Required[Iterable[Patch]]
    """List of patch operations to apply to the profile."""


class Patch(TypedDict, total=False):
    op: Required[str]
    """The operation to perform."""

    path: Required[str]
    """The JSON path specifying the part of the profile to operate on."""

    value: Required[str]
    """The value for the operation."""
