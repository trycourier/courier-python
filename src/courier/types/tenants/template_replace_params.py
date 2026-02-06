# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TemplateReplaceParams"]


class TemplateReplaceParams(TypedDict, total=False):
    tenant_id: Required[str]

    template: Required["TenantTemplateInputParam"]
    """Template configuration for creating or updating a tenant notification template"""

    published: bool
    """Whether to publish the template immediately after saving.

    When true, the template becomes the active/published version. When false
    (default), the template is saved as a draft.
    """


from ..tenant_template_input_param import TenantTemplateInputParam
