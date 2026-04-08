# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.paging import Paging
from .notification_template_summary import NotificationTemplateSummary

__all__ = ["AssociatedNotificationListResponse"]


class AssociatedNotificationListResponse(BaseModel):
    """Paginated list of notification templates associated with a routing strategy."""

    paging: Paging

    results: List[NotificationTemplateSummary]
