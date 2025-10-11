# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.tenant_association import TenantAssociation

__all__ = ["TenantAddMultipleParams"]


class TenantAddMultipleParams(TypedDict, total=False):
    tenants: Required[Iterable[TenantAssociation]]
