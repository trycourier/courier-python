# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.base_check import BaseCheck

__all__ = ["CheckUpdateParams"]


class CheckUpdateParams(TypedDict, total=False):
    id: Required[str]

    checks: Required[Iterable[BaseCheck]]
