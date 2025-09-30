# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AutomationStepParam"]

_AutomationStepParamReservedKeywords = TypedDict(
    "_AutomationStepParamReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class AutomationStepParam(_AutomationStepParamReservedKeywords, total=False):
    ref: Optional[str]
