# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["Locales", "LocalesItem"]


class LocalesItem(TypedDict, total=False):
    content: Required[str]


Locales: TypeAlias = Dict[str, LocalesItem]
