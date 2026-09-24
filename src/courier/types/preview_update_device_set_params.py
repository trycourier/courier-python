# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PreviewUpdateDeviceSetParams"]


class PreviewUpdateDeviceSetParams(TypedDict, total=False):
    device_ids: Required[SequenceNotStr[str]]
    """The devices the set contains, by `PreviewDevice.id`. At least one is required."""

    name: Required[str]
    """Human-readable name."""
