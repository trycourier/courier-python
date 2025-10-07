# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .invoke import (
    InvokeResource,
    AsyncInvokeResource,
    InvokeResourceWithRawResponse,
    AsyncInvokeResourceWithRawResponse,
    InvokeResourceWithStreamingResponse,
    AsyncInvokeResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AutomationsResource", "AsyncAutomationsResource"]


class AutomationsResource(SyncAPIResource):
    @cached_property
    def invoke(self) -> InvokeResource:
        return InvokeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AutomationsResourceWithStreamingResponse(self)


class AsyncAutomationsResource(AsyncAPIResource):
    @cached_property
    def invoke(self) -> AsyncInvokeResource:
        return AsyncInvokeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncAutomationsResourceWithStreamingResponse(self)


class AutomationsResourceWithRawResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

    @cached_property
    def invoke(self) -> InvokeResourceWithRawResponse:
        return InvokeResourceWithRawResponse(self._automations.invoke)


class AsyncAutomationsResourceWithRawResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

    @cached_property
    def invoke(self) -> AsyncInvokeResourceWithRawResponse:
        return AsyncInvokeResourceWithRawResponse(self._automations.invoke)


class AutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

    @cached_property
    def invoke(self) -> InvokeResourceWithStreamingResponse:
        return InvokeResourceWithStreamingResponse(self._automations.invoke)


class AsyncAutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

    @cached_property
    def invoke(self) -> AsyncInvokeResourceWithStreamingResponse:
        return AsyncInvokeResourceWithStreamingResponse(self._automations.invoke)
