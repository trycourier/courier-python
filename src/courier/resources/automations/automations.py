# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .invoke import (
    InvokeResource,
    AsyncInvokeResource,
    InvokeResourceWithRawResponse,
    AsyncInvokeResourceWithRawResponse,
    InvokeResourceWithStreamingResponse,
    AsyncInvokeResourceWithStreamingResponse,
)
from ...types import automation_list_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.automation_template_list_response import AutomationTemplateListResponse

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

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        version: Literal["published", "draft"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationTemplateListResponse:
        """Get the list of automations.

        Args:
          cursor: A cursor token for pagination.

        Use the cursor from the previous response to
              fetch the next page of results.

          version: The version of templates to retrieve. Accepted values are published (for
              published templates) or draft (for draft templates). Defaults to published.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/automations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "version": version,
                    },
                    automation_list_params.AutomationListParams,
                ),
            ),
            cast_to=AutomationTemplateListResponse,
        )


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

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        version: Literal["published", "draft"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationTemplateListResponse:
        """Get the list of automations.

        Args:
          cursor: A cursor token for pagination.

        Use the cursor from the previous response to
              fetch the next page of results.

          version: The version of templates to retrieve. Accepted values are published (for
              published templates) or draft (for draft templates). Defaults to published.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/automations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "version": version,
                    },
                    automation_list_params.AutomationListParams,
                ),
            ),
            cast_to=AutomationTemplateListResponse,
        )


class AutomationsResourceWithRawResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.list = to_raw_response_wrapper(
            automations.list,
        )

    @cached_property
    def invoke(self) -> InvokeResourceWithRawResponse:
        return InvokeResourceWithRawResponse(self._automations.invoke)


class AsyncAutomationsResourceWithRawResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.list = async_to_raw_response_wrapper(
            automations.list,
        )

    @cached_property
    def invoke(self) -> AsyncInvokeResourceWithRawResponse:
        return AsyncInvokeResourceWithRawResponse(self._automations.invoke)


class AutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.list = to_streamed_response_wrapper(
            automations.list,
        )

    @cached_property
    def invoke(self) -> InvokeResourceWithStreamingResponse:
        return InvokeResourceWithStreamingResponse(self._automations.invoke)


class AsyncAutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.list = async_to_streamed_response_wrapper(
            automations.list,
        )

    @cached_property
    def invoke(self) -> AsyncInvokeResourceWithStreamingResponse:
        return AsyncInvokeResourceWithStreamingResponse(self._automations.invoke)
