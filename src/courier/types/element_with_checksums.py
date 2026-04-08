# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ElementWithChecksums", "Locales"]


class Locales(BaseModel):
    checksum: str


class ElementWithChecksums(BaseModel):
    """
    An element with its content checksum and optional nested elements and locale checksums.
    """

    checksum: str
    """MD5 hash of translatable content."""

    type: str
    """Element type (text, meta, action, etc.)."""

    id: Optional[str] = None

    elements: Optional[List["ElementWithChecksums"]] = None
    """Nested child elements (for group-type elements)."""

    locales: Optional[Dict[str, Locales]] = None
    """Locale-specific content with checksums."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
