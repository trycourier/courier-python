# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .draft import (
    DraftResource,
    AsyncDraftResource,
    DraftResourceWithRawResponse,
    AsyncDraftResourceWithRawResponse,
    DraftResourceWithStreamingResponse,
    AsyncDraftResourceWithStreamingResponse,
)
from .checks import (
    ChecksResource,
    AsyncChecksResource,
    ChecksResourceWithRawResponse,
    AsyncChecksResourceWithRawResponse,
    ChecksResourceWithStreamingResponse,
    AsyncChecksResourceWithStreamingResponse,
)
from ...types import notification_list_params
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
from ...types.notification_get_content import NotificationGetContent
from ...types.notification_list_response import NotificationListResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def draft(self) -> DraftResource:
        return DraftResource(self._client)

    @cached_property
    def checks(self) -> ChecksResource:
        return ChecksResource(self._client)

    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        notes: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListResponse:
        """
        Args:
          notes: Retrieve the notes from the Notification template settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "notes": notes,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

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
            f"/notifications/{id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationGetContent,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def draft(self) -> AsyncDraftResource:
        return AsyncDraftResource(self._client)

    @cached_property
    def checks(self) -> AsyncChecksResource:
        return AsyncChecksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        notes: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListResponse:
        """
        Args:
          notes: Retrieve the notes from the Notification template settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "notes": notes,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

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
            f"/notifications/{id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationGetContent,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_raw_response_wrapper(
            notifications.list,
        )
        self.retrieve_content = to_raw_response_wrapper(
            notifications.retrieve_content,
        )

    @cached_property
    def draft(self) -> DraftResourceWithRawResponse:
        return DraftResourceWithRawResponse(self._notifications.draft)

    @cached_property
    def checks(self) -> ChecksResourceWithRawResponse:
        return ChecksResourceWithRawResponse(self._notifications.checks)


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_raw_response_wrapper(
            notifications.list,
        )
        self.retrieve_content = async_to_raw_response_wrapper(
            notifications.retrieve_content,
        )

    @cached_property
    def draft(self) -> AsyncDraftResourceWithRawResponse:
        return AsyncDraftResourceWithRawResponse(self._notifications.draft)

    @cached_property
    def checks(self) -> AsyncChecksResourceWithRawResponse:
        return AsyncChecksResourceWithRawResponse(self._notifications.checks)


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_streamed_response_wrapper(
            notifications.list,
        )
        self.retrieve_content = to_streamed_response_wrapper(
            notifications.retrieve_content,
        )

    @cached_property
    def draft(self) -> DraftResourceWithStreamingResponse:
        return DraftResourceWithStreamingResponse(self._notifications.draft)

    @cached_property
    def checks(self) -> ChecksResourceWithStreamingResponse:
        return ChecksResourceWithStreamingResponse(self._notifications.checks)


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_streamed_response_wrapper(
            notifications.list,
        )
        self.retrieve_content = async_to_streamed_response_wrapper(
            notifications.retrieve_content,
        )

    @cached_property
    def draft(self) -> AsyncDraftResourceWithStreamingResponse:
        return AsyncDraftResourceWithStreamingResponse(self._notifications.draft)

    @cached_property
    def checks(self) -> AsyncChecksResourceWithStreamingResponse:
        return AsyncChecksResourceWithStreamingResponse(self._notifications.checks)
