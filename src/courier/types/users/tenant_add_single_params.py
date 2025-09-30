# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TenantAddSingleParams"]


class TenantAddSingleParams(TypedDict, total=False):
    user_id: Required[str]

    profile: Optional[Dict[str, object]]
