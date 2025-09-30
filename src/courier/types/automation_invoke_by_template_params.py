# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["AutomationInvokeByTemplateParams"]


class AutomationInvokeByTemplateParams(TypedDict, total=False):
    brand: Optional[str]

    data: Optional[Dict[str, object]]

    profile: object

    recipient: Optional[str]

    template: Optional[str]
