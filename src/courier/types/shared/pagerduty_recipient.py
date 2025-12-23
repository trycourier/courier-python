# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .pagerduty import Pagerduty

__all__ = ["PagerdutyRecipient"]


class PagerdutyRecipient(BaseModel):
    """Send via PagerDuty"""

    pagerduty: Pagerduty
