# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ElementalContentSugar"]


class ElementalContentSugar(TypedDict, total=False):
    """Syntactic sugar to provide a fast shorthand for Courier Elemental Blocks."""

    body: Required[str]
    """The text content displayed in the notification."""

    title: Required[str]
    """Title/subject displayed by supported channels."""
