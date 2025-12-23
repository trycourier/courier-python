# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["ListPatternRecipient"]


class ListPatternRecipient(BaseModel):
    """Send to users in lists matching a pattern"""

    data: Optional[Dict[str, object]] = None

    list_pattern: Optional[str] = None
