# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..shared.channel_classification import ChannelClassification

__all__ = ["PreferenceBulkUpdateParams", "Topic"]


class PreferenceBulkUpdateParams(TypedDict, total=False):
    topics: Required[Iterable[Topic]]
    """The topics to create or update.

    Between 1 and 50 topics may be provided in a single request.
    """

    tenant_id: Optional[str]
    """Update the preferences of a user for this specific tenant context."""


class Topic(TypedDict, total=False):
    status: Required[Literal["OPTED_IN", "OPTED_OUT"]]
    """The subscription status to apply for this topic."""

    topic_id: Required[str]
    """A unique identifier associated with a subscription topic."""

    custom_routing: List[ChannelClassification]
    """The channels a user has chosen to receive notifications through for this topic."""

    has_custom_routing: bool
    """Whether the recipient has chosen specific delivery channels for this topic."""
