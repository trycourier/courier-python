# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .version_node import VersionNode
from .shared.paging import Paging

__all__ = ["NotificationTemplateVersionListResponse"]


class NotificationTemplateVersionListResponse(BaseModel):
    paging: Paging

    versions: List[VersionNode]
