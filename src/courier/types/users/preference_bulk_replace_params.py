# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..shared.channel_classification import ChannelClassification

__all__ = ["PreferenceBulkReplaceParams", "Topic"]


class PreferenceBulkReplaceParams(TypedDict, total=False):
    topics: Required[Iterable[Topic]]
    """The complete set of topic overrides for the user.

    Up to 50 topics may be provided. Any existing override not listed here is reset
    to its topic default; an empty array resets every existing override.
    """

    tenant_id: Optional[str]
    """Replace the preferences of a user for this specific tenant context."""


class Topic(TypedDict, total=False):
    status: Required[Literal["OPTED_IN", "OPTED_OUT"]]
    """The subscription status to apply for this topic."""

    topic_id: Required[str]
    """A unique identifier associated with a subscription topic."""

    custom_routing: List[ChannelClassification]
    """The channels a user has chosen to receive notifications through for this topic."""

    has_custom_routing: bool
    """Whether the recipient has chosen specific delivery channels for this topic."""
