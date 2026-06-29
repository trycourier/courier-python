# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["CancelJourneyRequestParam", "ByCancelationToken", "ByRunID"]


class ByCancelationToken(TypedDict, total=False):
    cancelation_token: Required[str]


class ByRunID(TypedDict, total=False):
    run_id: Required[str]


CancelJourneyRequestParam: TypeAlias = Union[ByCancelationToken, ByRunID]
