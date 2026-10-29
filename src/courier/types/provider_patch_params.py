# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProviderPatchParams", "Patch"]


class ProviderPatchParams(TypedDict, total=False):
    patch: Required[Iterable[Patch]]
    """Operations to apply, in order.

    Paths address the provider as it is returned: `/title`, `/alias`, `/provider`,
    and `/settings/<key>` with the snake_case setting keys, including nested paths
    such as `/settings/rate_limit/rate`. If any operation fails, for example a
    `test`, nothing is saved and the request returns a 400. The result can't change
    `provider`, remove `title`, or add other top-level fields. Removing `/alias`
    clears it.
    """


_PatchReservedKeywords = TypedDict(
    "_PatchReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Patch(_PatchReservedKeywords, total=False):
    """One JSON Patch (RFC 6902) operation."""

    op: Required[Literal["add", "remove", "replace", "move", "copy", "test"]]
    """The operation to perform."""

    path: Required[str]
    """JSON Pointer to the field to operate on, such as `/settings/api_key`."""

    value: object
    """The value for `add`, `replace` and `test`. Any JSON value."""
