# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..shared.channel_classification import ChannelClassification

__all__ = ["ChannelPreference"]


class ChannelPreference(TypedDict, total=False):
    channel: Required[ChannelClassification]
