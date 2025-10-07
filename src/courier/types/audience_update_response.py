# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .audience import Audience

__all__ = ["AudienceUpdateResponse"]


class AudienceUpdateResponse(BaseModel):
    audience: Audience
