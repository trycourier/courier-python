# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["FilterConfig"]


class FilterConfig(BaseModel):
    """
    A filter rule that can be either a single condition (with path/value) or a  nested group (with filters array). Use comparison operators (EQ, GT, etc.)  for single conditions, and logical operators (AND, OR) for nested groups.
    """

    operator: str
    """The operator for this filter.

    Use comparison operators (EQ, GT, LT, GTE, LTE, NEQ, EXISTS, INCLUDES,
    STARTS_WITH, ENDS_WITH, IS_BEFORE, IS_AFTER, OMIT) for single conditions, or
    logical operators (AND, OR) for nested filter groups.
    """

    filters: Optional[List["FilterConfig"]] = None
    """Nested filter rules to combine with AND/OR.

    Required for nested filter groups, not used for single filter conditions.
    """

    path: Optional[str] = None
    """The attribute path from the user profile to filter on.

    Required for single filter conditions, not used for nested filter groups.
    """

    value: Optional[str] = None
    """The value to compare against.

    Required for single filter conditions, not used for nested filter groups.
    """
