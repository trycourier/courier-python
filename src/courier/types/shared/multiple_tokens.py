# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from ..._models import BaseModel

__all__ = ["MultipleTokens"]


class MultipleTokens(BaseModel):
    tokens: Union[str, List[str]]
    """One device token, or an array of them.

    The values are the token strings themselves — not objects.
    """
