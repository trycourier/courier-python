# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AutomationListParams"]


class AutomationListParams(TypedDict, total=False):
    cursor: str
    """A cursor token for pagination.

    Use the cursor from the previous response to fetch the next page of results.
    """

    version: Literal["published", "draft"]
    """The version of templates to retrieve.

    Accepted values are published (for published templates) or draft (for draft
    templates). Defaults to published.
    """
