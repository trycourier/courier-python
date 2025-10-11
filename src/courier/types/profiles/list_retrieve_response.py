# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from ..shared.recipient_preferences import RecipientPreferences

__all__ = ["ListRetrieveResponse", "Result"]


class Result(BaseModel):
    id: str

    created: str
    """The date/time of when the list was created.

    Represented as a string in ISO format.
    """

    name: str
    """List name"""

    updated: str
    """The date/time of when the list was updated.

    Represented as a string in ISO format.
    """

    preferences: Optional[RecipientPreferences] = None


class ListRetrieveResponse(BaseModel):
    paging: Paging

    results: List[Result]
    """An array of lists"""
