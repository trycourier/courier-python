# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailParam"]


class EmailParam(TypedDict, total=False):
    footer: Required[object]

    header: Required[object]
