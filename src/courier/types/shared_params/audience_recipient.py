# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .audience_filter import AudienceFilter

__all__ = ["AudienceRecipient"]


class AudienceRecipient(TypedDict, total=False):
    """Send to all users in an audience"""

    audience_id: Required[str]
    """A unique identifier associated with an Audience.

    A message will be sent to each user in the audience.
    """

    data: Optional[Dict[str, object]]

    filters: Optional[Iterable[AudienceFilter]]
