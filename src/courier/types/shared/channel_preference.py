# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .channel_classification import ChannelClassification

__all__ = ["ChannelPreference"]


class ChannelPreference(BaseModel):
    channel: ChannelClassification
