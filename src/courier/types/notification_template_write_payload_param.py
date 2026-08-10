# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .notification_template_payload_param import NotificationTemplatePayloadParam

__all__ = ["NotificationTemplateWritePayloadParam"]


class NotificationTemplateWritePayloadParam(NotificationTemplatePayloadParam, total=False):
    """
    Template fields accepted in POST and PUT request bodies, nested under a `notification` key.
    """

    alias: Optional[str]
    """Send-time alias for this template — the value you pass as `event` to POST /send.

    Writes accept a single alias only. Optional, with three distinct meanings. Omit
    it to leave any existing aliases untouched. Send a string to make this the
    template's only alias — a template that already resolved from several aliases
    keeps just this one and the rest are detached. Send null to remove every alias
    from the template. An alias may not be claimed by another template — doing so
    returns 409 — and may not begin with "tenant/".
    """
