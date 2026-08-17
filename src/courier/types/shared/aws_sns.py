# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AwsSns"]


class AwsSns(BaseModel):
    """Routes a push notification through the AWS SNS provider.

    The target ARN must be nested under `aws_sns` — a top-level `target_arn` on the profile is ignored by the provider.
    """

    target_arn: str
    """The ARN of the SNS platform endpoint, topic, or application to publish to."""
