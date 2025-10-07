# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.notification_get_content import NotificationGetContent

__all__ = ["DraftResource", "AsyncDraftResource"]


class DraftResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return DraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return DraftResourceWithStreamingResponse(self)

    def retrieve_content(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationGetContent:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/notifications/{id}/draft/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationGetContent,
        )


class AsyncDraftResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncDraftResourceWithStreamingResponse(self)

    async def retrieve_content(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationGetContent:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/notifications/{id}/draft/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationGetContent,
        )


class DraftResourceWithRawResponse:
    def __init__(self, draft: DraftResource) -> None:
        self._draft = draft

        self.retrieve_content = to_raw_response_wrapper(
            draft.retrieve_content,
        )


class AsyncDraftResourceWithRawResponse:
    def __init__(self, draft: AsyncDraftResource) -> None:
        self._draft = draft

        self.retrieve_content = async_to_raw_response_wrapper(
            draft.retrieve_content,
        )


class DraftResourceWithStreamingResponse:
    def __init__(self, draft: DraftResource) -> None:
        self._draft = draft

        self.retrieve_content = to_streamed_response_wrapper(
            draft.retrieve_content,
        )


class AsyncDraftResourceWithStreamingResponse:
    def __init__(self, draft: AsyncDraftResource) -> None:
        self._draft = draft

        self.retrieve_content = async_to_streamed_response_wrapper(
            draft.retrieve_content,
        )
