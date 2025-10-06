# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["InvokeInvokeByTemplateParams"]


class InvokeInvokeByTemplateParams(TypedDict, total=False):
    recipient: Required[Optional[str]]

    brand: Optional[str]

    data: Optional[Dict[str, object]]

    profile: Optional[Dict[str, object]]

    template: Optional[str]
