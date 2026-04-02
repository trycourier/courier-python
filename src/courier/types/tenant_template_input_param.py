# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.message_channels import MessageChannels
from .shared_params.elemental_content import ElementalContent
from .shared_params.message_providers import MessageProviders

__all__ = ["TenantTemplateInputParam"]


class TenantTemplateInputParam(TypedDict, total=False):
    """Template configuration for creating or updating a tenant notification template"""

    content: Required[ElementalContent]
    """
    Template content configuration including blocks, elements, and message structure
    """

    channels: MessageChannels
    """Channel-specific delivery configuration (email, SMS, push, etc.)"""

    providers: MessageProviders
    """
    Provider-specific delivery configuration for routing to specific email/SMS
    providers
    """

    routing: "MessageRouting"
    """Message routing configuration for multi-channel delivery strategies"""


from .shared_params.message_routing import MessageRouting
