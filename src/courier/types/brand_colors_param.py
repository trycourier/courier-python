# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrandColorsParam"]


class BrandColorsParam(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=str,  # pyright: ignore[reportGeneralTypeIssues]
):
    primary: str

    secondary: str
