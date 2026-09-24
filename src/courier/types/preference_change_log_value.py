# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.preference_status import PreferenceStatus
from .shared.channel_classification import ChannelClassification

__all__ = ["PreferenceChangeLogValue"]


class PreferenceChangeLogValue(BaseModel):
    custom_routing: List[ChannelClassification]
    """The channels chosen before the change."""

    has_custom_routing: bool
    """Whether custom routing was in effect before the change."""

    status: PreferenceStatus
    """The subscription status before the change."""
