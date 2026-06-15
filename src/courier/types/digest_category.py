# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DigestCategory"]


class DigestCategory(BaseModel):
    category_key: str
    """The key that identifies the category within the digest."""

    retain: Literal["first", "last", "highest", "lowest", "none"]
    """
    Which events to keep when the number of events exceeds the retention limit for
    the category.
    """

    sort_key: Optional[str] = None
    """The data key used to order events when `retain` is `highest` or `lowest`."""
