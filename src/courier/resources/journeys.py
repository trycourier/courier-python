# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import journey_list_params, journey_invoke_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.journeys_list_response import JourneysListResponse
from ..types.journeys_invoke_response import JourneysInvokeResponse

__all__ = ["JourneysResource", "AsyncJourneysResource"]


class JourneysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JourneysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return JourneysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JourneysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return JourneysResourceWithStreamingResponse(self)

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
    ) -> JourneysListResponse:
        """Get the list of journeys.

        Args:
          cursor: A cursor token for pagination.

        Use the cursor from the previous response to
              fetch the next page of results.

          version: The version of journeys to retrieve. Accepted values are published (for
              published journeys) or draft (for draft journeys). Defaults to published.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/journeys",
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
                    journey_list_params.JourneyListParams,
                ),
            ),
            cast_to=JourneysListResponse,
        )

    def invoke(
        self,
        template_id: str,
        *,
        data: Dict[str, object] | Omit = omit,
        profile: Dict[str, object] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneysInvokeResponse:
        """
        Invoke a journey run from a journey template.

        Args:
          data: Data payload passed to the journey. The expected shape can be predefined using
              the schema builder in the journey editor. This data is available in journey
              steps for condition evaluation and template variable interpolation. Can also
              contain user identifiers (user_id, userId, anonymousId) if not provided
              elsewhere.

          profile: Profile data for the user. Can contain contact information (email,
              phone_number), user identifiers (user_id, userId, anonymousId), or any custom
              profile fields. Profile fields are merged with any existing stored profile for
              the user. Include context.tenant_id to load a tenant-scoped profile for
              multi-tenant scenarios.

          user_id: A unique identifier for the user. If not provided, the system will attempt to
              resolve the user identifier from profile or data objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._post(
            f"/journeys/{template_id}/invoke",
            body=maybe_transform(
                {
                    "data": data,
                    "profile": profile,
                    "user_id": user_id,
                },
                journey_invoke_params.JourneyInvokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneysInvokeResponse,
        )


class AsyncJourneysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJourneysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJourneysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJourneysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncJourneysResourceWithStreamingResponse(self)

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
    ) -> JourneysListResponse:
        """Get the list of journeys.

        Args:
          cursor: A cursor token for pagination.

        Use the cursor from the previous response to
              fetch the next page of results.

          version: The version of journeys to retrieve. Accepted values are published (for
              published journeys) or draft (for draft journeys). Defaults to published.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/journeys",
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
                    journey_list_params.JourneyListParams,
                ),
            ),
            cast_to=JourneysListResponse,
        )

    async def invoke(
        self,
        template_id: str,
        *,
        data: Dict[str, object] | Omit = omit,
        profile: Dict[str, object] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneysInvokeResponse:
        """
        Invoke a journey run from a journey template.

        Args:
          data: Data payload passed to the journey. The expected shape can be predefined using
              the schema builder in the journey editor. This data is available in journey
              steps for condition evaluation and template variable interpolation. Can also
              contain user identifiers (user_id, userId, anonymousId) if not provided
              elsewhere.

          profile: Profile data for the user. Can contain contact information (email,
              phone_number), user identifiers (user_id, userId, anonymousId), or any custom
              profile fields. Profile fields are merged with any existing stored profile for
              the user. Include context.tenant_id to load a tenant-scoped profile for
              multi-tenant scenarios.

          user_id: A unique identifier for the user. If not provided, the system will attempt to
              resolve the user identifier from profile or data objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._post(
            f"/journeys/{template_id}/invoke",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "profile": profile,
                    "user_id": user_id,
                },
                journey_invoke_params.JourneyInvokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneysInvokeResponse,
        )


class JourneysResourceWithRawResponse:
    def __init__(self, journeys: JourneysResource) -> None:
        self._journeys = journeys

        self.list = to_raw_response_wrapper(
            journeys.list,
        )
        self.invoke = to_raw_response_wrapper(
            journeys.invoke,
        )


class AsyncJourneysResourceWithRawResponse:
    def __init__(self, journeys: AsyncJourneysResource) -> None:
        self._journeys = journeys

        self.list = async_to_raw_response_wrapper(
            journeys.list,
        )
        self.invoke = async_to_raw_response_wrapper(
            journeys.invoke,
        )


class JourneysResourceWithStreamingResponse:
    def __init__(self, journeys: JourneysResource) -> None:
        self._journeys = journeys

        self.list = to_streamed_response_wrapper(
            journeys.list,
        )
        self.invoke = to_streamed_response_wrapper(
            journeys.invoke,
        )


class AsyncJourneysResourceWithStreamingResponse:
    def __init__(self, journeys: AsyncJourneysResource) -> None:
        self._journeys = journeys

        self.list = async_to_streamed_response_wrapper(
            journeys.list,
        )
        self.invoke = async_to_streamed_response_wrapper(
            journeys.invoke,
        )
