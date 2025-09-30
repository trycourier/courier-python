# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MsTeamsBasePropertiesParam"]


class MsTeamsBasePropertiesParam(TypedDict, total=False):
    service_url: Required[str]

    tenant_id: Required[str]
