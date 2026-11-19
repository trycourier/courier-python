# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import feedback_create_params
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
from ..types.feedback_create_response import FeedbackCreateResponse

__all__ = ["FeedbackResource", "AsyncFeedbackResource"]


class FeedbackResource(SyncAPIResource):
    """
    Report suspected bugs, confusing behavior and missing features in Courier, from an AI agent, a developer tool or by hand.
    """

    @cached_property
    def with_raw_response(self) -> FeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return FeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return FeedbackResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        category: Literal["possible_bug", "confusing_behavior", "feature_request", "other"],
        description: str,
        surface: Literal["api", "sdk", "mcp", "ui", "docs", "other"],
        title: str,
        expected_behavior: str | Omit = omit,
        harness: str | Omit = omit,
        location: str | Omit = omit,
        model: str | Omit = omit,
        request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedbackCreateResponse:
        """Reports a suspected bug, confusing behavior or a missing feature in Courier.

        It
        is built for AI agents and developer tools to call when Courier does something
        unexpected, and people can call it too.

        A report is not a support ticket. A `201` means Courier stored the report; it
        does not promise a reply or a fix. For help with your account, contact Courier
        support.

        Never include secrets, API keys or customer data such as recipient names, email
        addresses or message content.

        Requires an API key with no scope restrictions; a JWT or a scoped API key is
        refused. Each workspace can submit 200 reports per UTC day, and requests that
        fail validation count toward that limit.

        Args:
          category: What kind of report this is: `possible_bug` for behavior that looks wrong,
              `confusing_behavior` for behavior that works but was hard to understand,
              `feature_request` for something Courier does not do yet, and `other`.

          description: What happened, in enough detail for someone at Courier to follow it.

          surface: Where you met the problem: the REST `api`, an `sdk`, the Courier `mcp` server,
              the Courier app `ui`, the `docs`, or `other`.

          title: A one-line summary of the report.

          expected_behavior: What you expected to happen instead.

          harness: The agent or tool that submitted the report, such as `Claude Code`.

          location: Where it happened, such as an endpoint (`POST /send`), an SDK method, an MCP
              tool name or a docs URL.

          model: The AI model that submitted the report, such as `claude-opus-5-5`.

          request_id: The request ID of an API call that shows the problem, if there is one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/feedback",
            body=maybe_transform(
                {
                    "category": category,
                    "description": description,
                    "surface": surface,
                    "title": title,
                    "expected_behavior": expected_behavior,
                    "harness": harness,
                    "location": location,
                    "model": model,
                    "request_id": request_id,
                },
                feedback_create_params.FeedbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackCreateResponse,
        )


class AsyncFeedbackResource(AsyncAPIResource):
    """
    Report suspected bugs, confusing behavior and missing features in Courier, from an AI agent, a developer tool or by hand.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncFeedbackResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        category: Literal["possible_bug", "confusing_behavior", "feature_request", "other"],
        description: str,
        surface: Literal["api", "sdk", "mcp", "ui", "docs", "other"],
        title: str,
        expected_behavior: str | Omit = omit,
        harness: str | Omit = omit,
        location: str | Omit = omit,
        model: str | Omit = omit,
        request_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedbackCreateResponse:
        """Reports a suspected bug, confusing behavior or a missing feature in Courier.

        It
        is built for AI agents and developer tools to call when Courier does something
        unexpected, and people can call it too.

        A report is not a support ticket. A `201` means Courier stored the report; it
        does not promise a reply or a fix. For help with your account, contact Courier
        support.

        Never include secrets, API keys or customer data such as recipient names, email
        addresses or message content.

        Requires an API key with no scope restrictions; a JWT or a scoped API key is
        refused. Each workspace can submit 200 reports per UTC day, and requests that
        fail validation count toward that limit.

        Args:
          category: What kind of report this is: `possible_bug` for behavior that looks wrong,
              `confusing_behavior` for behavior that works but was hard to understand,
              `feature_request` for something Courier does not do yet, and `other`.

          description: What happened, in enough detail for someone at Courier to follow it.

          surface: Where you met the problem: the REST `api`, an `sdk`, the Courier `mcp` server,
              the Courier app `ui`, the `docs`, or `other`.

          title: A one-line summary of the report.

          expected_behavior: What you expected to happen instead.

          harness: The agent or tool that submitted the report, such as `Claude Code`.

          location: Where it happened, such as an endpoint (`POST /send`), an SDK method, an MCP
              tool name or a docs URL.

          model: The AI model that submitted the report, such as `claude-opus-5-5`.

          request_id: The request ID of an API call that shows the problem, if there is one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/feedback",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "description": description,
                    "surface": surface,
                    "title": title,
                    "expected_behavior": expected_behavior,
                    "harness": harness,
                    "location": location,
                    "model": model,
                    "request_id": request_id,
                },
                feedback_create_params.FeedbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackCreateResponse,
        )


class FeedbackResourceWithRawResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create = to_raw_response_wrapper(
            feedback.create,
        )


class AsyncFeedbackResourceWithRawResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create = async_to_raw_response_wrapper(
            feedback.create,
        )


class FeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create = to_streamed_response_wrapper(
            feedback.create,
        )


class AsyncFeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create = async_to_streamed_response_wrapper(
            feedback.create,
        )
