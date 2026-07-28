# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["JourneyCancelParams", "ByCancelationToken", "ByRunID"]


class ByCancelationToken(TypedDict, total=False):
    cancelation_token: Required[str]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]


class ByRunID(TypedDict, total=False):
    run_id: Required[str]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]


JourneyCancelParams: TypeAlias = Union[ByCancelationToken, ByRunID]
