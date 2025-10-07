# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .filter import Filter
from .._models import BaseModel

__all__ = ["Audience"]


class Audience(BaseModel):
    id: str
    """A unique identifier representing the audience_id"""

    created_at: str

    description: str
    """A description of the audience"""

    filter: Filter
    """A single filter to use for filtering"""

    name: str
    """The name of the audience"""

    updated_at: str
