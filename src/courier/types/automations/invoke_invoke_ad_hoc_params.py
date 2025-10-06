# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InvokeInvokeAdHocParams",
    "Automation",
    "AutomationStep",
    "AutomationStepAutomationDelayStep",
    "AutomationStepAutomationSendStep",
    "AutomationStepAutomationSendListStep",
    "AutomationStepAutomationUpdateProfileStep",
    "AutomationStepAutomationCancelStep",
    "AutomationStepAutomationFetchDataStep",
    "AutomationStepAutomationFetchDataStepWebhook",
    "AutomationStepAutomationInvokeStep",
]


class InvokeInvokeAdHocParams(TypedDict, total=False):
    automation: Required[Automation]

    brand: Optional[str]

    data: Optional[Dict[str, object]]

    profile: Optional[Dict[str, object]]

    recipient: Optional[str]

    template: Optional[str]


class AutomationStepAutomationDelayStep(TypedDict, total=False):
    action: Required[Literal["delay"]]

    duration: Optional[str]

    until: Optional[str]


class AutomationStepAutomationSendStep(TypedDict, total=False):
    action: Required[Literal["send"]]

    brand: Optional[str]

    data: Optional[Dict[str, object]]

    profile: Optional[Dict[str, object]]

    recipient: Optional[str]

    template: Optional[str]


class AutomationStepAutomationSendListStep(TypedDict, total=False):
    action: Required[Literal["send-list"]]

    list: Required[str]

    brand: Optional[str]

    data: Optional[Dict[str, object]]


class AutomationStepAutomationUpdateProfileStep(TypedDict, total=False):
    action: Required[Literal["update-profile"]]

    profile: Required[Dict[str, object]]

    merge: Optional[Literal["none", "overwrite", "soft-merge", "replace"]]

    recipient_id: Optional[str]


class AutomationStepAutomationCancelStep(TypedDict, total=False):
    action: Required[Literal["cancel"]]

    cancelation_token: Required[str]


class AutomationStepAutomationFetchDataStepWebhook(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]]

    url: Required[str]

    body: Optional[str]

    headers: Optional[Dict[str, str]]


class AutomationStepAutomationFetchDataStep(TypedDict, total=False):
    action: Required[Literal["fetch-data"]]

    webhook: Required[AutomationStepAutomationFetchDataStepWebhook]

    merge_strategy: Optional[Literal["replace", "overwrite", "soft-merge"]]


class AutomationStepAutomationInvokeStep(TypedDict, total=False):
    action: Required[Literal["invoke"]]

    template: Required[str]


AutomationStep: TypeAlias = Union[
    AutomationStepAutomationDelayStep,
    AutomationStepAutomationSendStep,
    AutomationStepAutomationSendListStep,
    AutomationStepAutomationUpdateProfileStep,
    AutomationStepAutomationCancelStep,
    AutomationStepAutomationFetchDataStep,
    AutomationStepAutomationInvokeStep,
]


class Automation(TypedDict, total=False):
    steps: Required[Iterable[AutomationStep]]

    cancelation_token: Optional[str]
