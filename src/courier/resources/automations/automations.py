# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...types import automation_invoke_ad_hoc_params, automation_invoke_by_template_params
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
from ...types.automations.automation_invoke_response import AutomationInvokeResponse

__all__ = ["AutomationsResource", "AsyncAutomationsResource"]


class AutomationsResource(SyncAPIResource):
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

    def invoke_ad_hoc(
        self,
        *,
        automation: automation_invoke_ad_hoc_params.Automation,
        brand: Optional[str] | Omit = omit,
        data: Optional[Dict[str, object]] | Omit = omit,
        profile: object | Omit = omit,
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
                automation_invoke_ad_hoc_params.AutomationInvokeAdHocParams,
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
        brand: Optional[str] | Omit = omit,
        data: Optional[Dict[str, object]] | Omit = omit,
        profile: object | Omit = omit,
        recipient: Optional[str] | Omit = omit,
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
                    "brand": brand,
                    "data": data,
                    "profile": profile,
                    "recipient": recipient,
                    "template": template,
                },
                automation_invoke_by_template_params.AutomationInvokeByTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationInvokeResponse,
        )


class AsyncAutomationsResource(AsyncAPIResource):
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

    async def invoke_ad_hoc(
        self,
        *,
        automation: automation_invoke_ad_hoc_params.Automation,
        brand: Optional[str] | Omit = omit,
        data: Optional[Dict[str, object]] | Omit = omit,
        profile: object | Omit = omit,
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
                automation_invoke_ad_hoc_params.AutomationInvokeAdHocParams,
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
        brand: Optional[str] | Omit = omit,
        data: Optional[Dict[str, object]] | Omit = omit,
        profile: object | Omit = omit,
        recipient: Optional[str] | Omit = omit,
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
                    "brand": brand,
                    "data": data,
                    "profile": profile,
                    "recipient": recipient,
                    "template": template,
                },
                automation_invoke_by_template_params.AutomationInvokeByTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationInvokeResponse,
        )


class AutomationsResourceWithRawResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.invoke_ad_hoc = to_raw_response_wrapper(
            automations.invoke_ad_hoc,
        )
        self.invoke_by_template = to_raw_response_wrapper(
            automations.invoke_by_template,
        )


class AsyncAutomationsResourceWithRawResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.invoke_ad_hoc = async_to_raw_response_wrapper(
            automations.invoke_ad_hoc,
        )
        self.invoke_by_template = async_to_raw_response_wrapper(
            automations.invoke_by_template,
        )


class AutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.invoke_ad_hoc = to_streamed_response_wrapper(
            automations.invoke_ad_hoc,
        )
        self.invoke_by_template = to_streamed_response_wrapper(
            automations.invoke_by_template,
        )


class AsyncAutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.invoke_ad_hoc = async_to_streamed_response_wrapper(
            automations.invoke_ad_hoc,
        )
        self.invoke_by_template = async_to_streamed_response_wrapper(
            automations.invoke_by_template,
        )
