# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PreviewRunFailureReason"]

PreviewRunFailureReason: TypeAlias = Literal[
    "TEMPLATE_NOT_SUPPORTED", "NO_EMAIL_CHANNEL", "RENDER_FAILED", "ALL_DEVICES_UNSUPPORTED", "VENDOR_ERROR"
]
