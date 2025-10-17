# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

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
from ...types.automations import invoke_invoke_ad_hoc_params, invoke_invoke_by_template_params
from ...types.automation_invoke_response import AutomationInvokeResponse

__all__ = ["InvokeResource", "AsyncInvokeResource"]


class InvokeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvokeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return InvokeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvokeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return InvokeResourceWithStreamingResponse(self)

    def invoke_ad_hoc(
        self,
        *,
        automation: invoke_invoke_ad_hoc_params.Automation,
        brand: Optional[str] | Omit = omit,
        data: Optional[Dict[str, object]] | Omit = omit,
        profile: Optional[Dict[str, object]] | Omit = omit,
        recipient: Optional[str] | Omit = omit,
        template: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationInvokeResponse:
        """Invoke an ad hoc automation run.

        This endpoint accepts a JSON payload with a
        series of automation steps. For information about what steps are available,
        checkout the ad hoc automation guide
        [here](https://www.courier.com/docs/automations/steps/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/automations/invoke",
            body=maybe_transform(
                {
                    "automation": automation,
                    "brand": brand,
                    "data": data,
                    "profile": profile,
                    "recipient": recipient,
                    "template": template,
                },
                invoke_invoke_ad_hoc_params.InvokeInvokeAdHocParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationInvokeResponse,
        )

    def invoke_by_template(
        self,
        template_id: str,
        *,
        recipient: Optional[str],
        brand: Optional[str] | Omit = omit,
        data: Optional[Dict[str, object]] | Omit = omit,
        profile: Optional[Dict[str, object]] | Omit = omit,
        template: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationInvokeResponse:
        """
        Invoke an automation run from an automation template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._post(
            f"/automations/{template_id}/invoke",
            body=maybe_transform(
                {
                    "recipient": recipient,
                    "brand": brand,
                    "data": data,
                    "profile": profile,
                    "template": template,
                },
                invoke_invoke_by_template_params.InvokeInvokeByTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationInvokeResponse,
        )


class AsyncInvokeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvokeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvokeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvokeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncInvokeResourceWithStreamingResponse(self)

    async def invoke_ad_hoc(
        self,
        *,
        automation: invoke_invoke_ad_hoc_params.Automation,
        brand: Optional[str] | Omit = omit,
        data: Optional[Dict[str, object]] | Omit = omit,
        profile: Optional[Dict[str, object]] | Omit = omit,
        recipient: Optional[str] | Omit = omit,
        template: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationInvokeResponse:
        """Invoke an ad hoc automation run.

        This endpoint accepts a JSON payload with a
        series of automation steps. For information about what steps are available,
        checkout the ad hoc automation guide
        [here](https://www.courier.com/docs/automations/steps/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/automations/invoke",
            body=await async_maybe_transform(
                {
                    "automation": automation,
                    "brand": brand,
                    "data": data,
                    "profile": profile,
                    "recipient": recipient,
                    "template": template,
                },
                invoke_invoke_ad_hoc_params.InvokeInvokeAdHocParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationInvokeResponse,
        )

    async def invoke_by_template(
        self,
        template_id: str,
        *,
        recipient: Optional[str],
        brand: Optional[str] | Omit = omit,
        data: Optional[Dict[str, object]] | Omit = omit,
        profile: Optional[Dict[str, object]] | Omit = omit,
        template: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationInvokeResponse:
        """
        Invoke an automation run from an automation template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._post(
            f"/automations/{template_id}/invoke",
            body=await async_maybe_transform(
                {
                    "recipient": recipient,
                    "brand": brand,
                    "data": data,
                    "profile": profile,
                    "template": template,
                },
                invoke_invoke_by_template_params.InvokeInvokeByTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationInvokeResponse,
        )


class InvokeResourceWithRawResponse:
    def __init__(self, invoke: InvokeResource) -> None:
        self._invoke = invoke

        self.invoke_ad_hoc = to_raw_response_wrapper(
            invoke.invoke_ad_hoc,
        )
        self.invoke_by_template = to_raw_response_wrapper(
            invoke.invoke_by_template,
        )


class AsyncInvokeResourceWithRawResponse:
    def __init__(self, invoke: AsyncInvokeResource) -> None:
        self._invoke = invoke

        self.invoke_ad_hoc = async_to_raw_response_wrapper(
            invoke.invoke_ad_hoc,
        )
        self.invoke_by_template = async_to_raw_response_wrapper(
            invoke.invoke_by_template,
        )


class InvokeResourceWithStreamingResponse:
    def __init__(self, invoke: InvokeResource) -> None:
        self._invoke = invoke

        self.invoke_ad_hoc = to_streamed_response_wrapper(
            invoke.invoke_ad_hoc,
        )
        self.invoke_by_template = to_streamed_response_wrapper(
            invoke.invoke_by_template,
        )


class AsyncInvokeResourceWithStreamingResponse:
    def __init__(self, invoke: AsyncInvokeResource) -> None:
        self._invoke = invoke

        self.invoke_ad_hoc = async_to_streamed_response_wrapper(
            invoke.invoke_ad_hoc,
        )
        self.invoke_by_template = async_to_streamed_response_wrapper(
            invoke.invoke_by_template,
        )
