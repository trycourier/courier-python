# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Pagerduty"]


class Pagerduty(BaseModel):
    event_action: Optional[str] = None

    routing_key: Optional[str] = None

    severity: Optional[str] = None

    source: Optional[str] = None
