# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.paging import Paging
from .journey_template_summary import JourneyTemplateSummary

__all__ = ["JourneyTemplateListResponse"]


class JourneyTemplateListResponse(BaseModel):
    """Paged list of journey-scoped notification templates."""

    paging: Paging

    results: List[JourneyTemplateSummary]
