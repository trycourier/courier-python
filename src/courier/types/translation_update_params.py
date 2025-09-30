# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TranslationUpdateParams"]


class TranslationUpdateParams(TypedDict, total=False):
    domain: Required[str]

    body: Required[str]
