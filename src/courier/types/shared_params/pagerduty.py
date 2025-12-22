# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["Pagerduty"]


class Pagerduty(TypedDict, total=False):
    event_action: Optional[str]

    routing_key: Optional[str]

    severity: Optional[str]

    source: Optional[str]
