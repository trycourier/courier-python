# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .automation_template import AutomationTemplate

__all__ = ["AutomationTemplateListResponse"]


class AutomationTemplateListResponse(BaseModel):
    cursor: Optional[str] = None
    """A cursor token for pagination. Present when there are more results available."""

    templates: Optional[List[AutomationTemplate]] = None
