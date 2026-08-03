# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .journey_experiment import JourneyExperiment
from .journey_conditions_field import JourneyConditionsField

__all__ = ["JourneySendNode", "Message", "MessageContext", "MessageDelay", "MessageTo"]


class MessageContext(BaseModel):
    """Tenant context for this send.

    Set it to deliver on behalf of one of your customers, so the message uses that tenant's brand and settings.
    """

    tenant_id: str
    """The tenant to send as.

    Accepts either a literal tenant id (`acme-tenant`) or a whole-string mustache
    reference to a value the run already holds — `{{data.tenant_id}}` from the
    invocation payload, or `{{f1.body.tenant_id}}` from the response of an earlier
    fetch node with id `f1`. A reference is resolved separately on every run, so a
    single journey can deliver as many tenants. Two forms are rejected with `400`:
    mid-string interpolation such as `tenant-{{data.region}}`, and any value
    beginning with `refs.`, which is reserved for internal use. A reference that
    resolves to nothing at run time does not stop the run — the message is still
    sent, with no tenant context — so make sure the referenced value is always
    present. `GET` returns the value in the same form it was supplied.
    """


class MessageDelay(BaseModel):
    until: str

    timezone: Optional[str] = None


class MessageTo(BaseModel):
    email_override: Optional[str] = None

    phone_number_override: Optional[str] = None

    user_id_override: Optional[str] = None


class Message(BaseModel):
    context: Optional[MessageContext] = None
    """Tenant context for this send.

    Set it to deliver on behalf of one of your customers, so the message uses that
    tenant's brand and settings.
    """

    data: Optional[Dict[str, object]] = None

    delay: Optional[MessageDelay] = None

    template: Optional[str] = None

    to: Optional[MessageTo] = None


class JourneySendNode(BaseModel):
    """Send to the recipient.

    A send node sources its content from EXACTLY ONE of `message.template` (a single notification template) or `experiment` (an A/B split across weighted template variants) — supplying both, or neither, is rejected. Optionally override the recipient address, send as a tenant, delay the send, or attach `data`.
    """

    message: Message

    type: Literal["send"]

    id: Optional[str] = None

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    experiment: Optional[JourneyExperiment] = None
    """A/B experiment config for a send node.

    The recipient is deterministically bucketed by `bucketingKey` and routed to one
    of the `variants` in proportion to its `weight`. Present on a send node INSTEAD
    OF `message.template`.
    """
