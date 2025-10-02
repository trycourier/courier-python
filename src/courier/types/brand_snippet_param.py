# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrandSnippetParam"]


class BrandSnippetParam(TypedDict, total=False):
    format: Required[Literal["handlebars"]]

    name: Required[str]

    value: Required[str]
