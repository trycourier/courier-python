# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    NotificationTemplateState,
    broadcast_list_params,
    broadcast_send_params,
    broadcast_create_params,
    broadcast_update_params,
    broadcast_schedule_params,
    broadcast_put_content_params,
    broadcast_retrieve_content_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.broadcast import Broadcast
from ..types.broadcast_list_response import BroadcastListResponse
from ..types.notification_template_state import NotificationTemplateState
from ..types.notification_content_get_response import NotificationContentGetResponse
from ..types.notification_content_mutation_response import NotificationContentMutationResponse

__all__ = ["BroadcastsResource", "AsyncBroadcastsResource"]


class BroadcastsResource(SyncAPIResource):
    """
    Create a one-off send to a list or audience, author its content, then send it immediately or schedule it for later.
    """

    @cached_property
    def with_raw_response(self) -> BroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return BroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return BroadcastsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        channel: Literal["email", "sms", "push", "inbox", "slack", "msteams"],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Create a broadcast.

        Provisions a private notification template for the broadcast
        and returns the new broadcast in the draft state. Exactly one channel is
        required.

        Args:
          channel: The single delivery channel for this broadcast.

          name: Human-readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/broadcasts",
            body=maybe_transform(
                {
                    "channel": channel,
                    "name": name,
                },
                broadcast_create_params.BroadcastCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    def retrieve(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Retrieve a broadcast by ID.

        Archived broadcasts return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._get(
            path_template("/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    def update(
        self,
        broadcast_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Update a broadcast's name.

        Content is edited via the broadcast's notification
        template, not this endpoint.

        Args:
          name: New human-readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._put(
            path_template("/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            body=maybe_transform({"name": name}, broadcast_update_params.BroadcastUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastListResponse:
        """List broadcasts in your workspace.

        Cursor-paginated; returns broadcasts
        newest-first.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/broadcasts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    broadcast_list_params.BroadcastListParams,
                ),
            ),
            cast_to=BroadcastListResponse,
        )

    def archive(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Archive a broadcast.

        This is a soft delete — the archived broadcast is returned
        and no longer appears in list results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._delete(
            path_template("/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    def cancel(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Cancel a broadcast's pending schedule, returning it to the draft state.

        Only
        valid for a scheduled broadcast.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._post(
            path_template("/broadcasts/{broadcast_id}/cancel", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    def duplicate(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """
        Duplicate a broadcast (and its template) into a new draft named "{source name}
        (copy)".

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._post(
            path_template("/broadcasts/{broadcast_id}/duplicate", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    def put_content(
        self,
        broadcast_id: str,
        *,
        content: broadcast_put_content_params.Content,
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """
        Author the broadcast's content by replacing the draft elemental content of its
        private notification template. The draft is published automatically when the
        broadcast is sent or scheduled.

        Args:
          content: Elemental content payload. The server defaults `version` when omitted.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._put(
            path_template("/broadcasts/{broadcast_id}/content", broadcast_id=broadcast_id),
            body=maybe_transform(
                {
                    "content": content,
                    "state": state,
                },
                broadcast_put_content_params.BroadcastPutContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    def retrieve_content(
        self,
        broadcast_id: str,
        *,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentGetResponse:
        """
        Retrieve the broadcast's content — the elemental content of its private
        notification template. Defaults to the working draft, since broadcast content is
        authored as a draft until the broadcast is sent.

        Args:
          version: Accepts `draft`, `published`, or a version string (e.g. `v001`). Defaults to
              `draft`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._get(
            path_template("/broadcasts/{broadcast_id}/content", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"version": version}, broadcast_retrieve_content_params.BroadcastRetrieveContentParams
                ),
            ),
            cast_to=NotificationContentGetResponse,
        )

    def schedule(
        self,
        broadcast_id: str,
        *,
        recipient_id: str,
        recipient_type: Literal["list", "audience"],
        scheduled_to: str,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Schedule a broadcast for a future send to a list or audience.

        Publishes the
        broadcast template first. Not allowed once the broadcast is sending or sent. For
        an immediate send use POST /broadcasts/{broadcastId}/send.

        Args:
          recipient_id: ID of the target list or audience.

          recipient_type: Whether the broadcast targets a list or an audience.

          scheduled_to: Wall-clock timestamp of the future send, no timezone offset (e.g.
              "2026-07-21T20:00:00"). The zone is given by `timezone`.

          timezone: IANA timezone for the scheduled send (e.g. America/New_York).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._post(
            path_template("/broadcasts/{broadcast_id}/schedule", broadcast_id=broadcast_id),
            body=maybe_transform(
                {
                    "recipient_id": recipient_id,
                    "recipient_type": recipient_type,
                    "scheduled_to": scheduled_to,
                    "timezone": timezone,
                },
                broadcast_schedule_params.BroadcastScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    def send(
        self,
        broadcast_id: str,
        *,
        recipient_id: str,
        recipient_type: Literal["list", "audience"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Send a broadcast immediately to a list or audience.

        Publishes the broadcast
        template first. Not allowed once the broadcast is sending or sent.

        Args:
          recipient_id: ID of the target list or audience.

          recipient_type: Whether the broadcast targets a list or an audience.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return self._post(
            path_template("/broadcasts/{broadcast_id}/send", broadcast_id=broadcast_id),
            body=maybe_transform(
                {
                    "recipient_id": recipient_id,
                    "recipient_type": recipient_type,
                },
                broadcast_send_params.BroadcastSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )


class AsyncBroadcastsResource(AsyncAPIResource):
    """
    Create a one-off send to a list or audience, author its content, then send it immediately or schedule it for later.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBroadcastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncBroadcastsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        channel: Literal["email", "sms", "push", "inbox", "slack", "msteams"],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Create a broadcast.

        Provisions a private notification template for the broadcast
        and returns the new broadcast in the draft state. Exactly one channel is
        required.

        Args:
          channel: The single delivery channel for this broadcast.

          name: Human-readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/broadcasts",
            body=await async_maybe_transform(
                {
                    "channel": channel,
                    "name": name,
                },
                broadcast_create_params.BroadcastCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    async def retrieve(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Retrieve a broadcast by ID.

        Archived broadcasts return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._get(
            path_template("/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    async def update(
        self,
        broadcast_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Update a broadcast's name.

        Content is edited via the broadcast's notification
        template, not this endpoint.

        Args:
          name: New human-readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._put(
            path_template("/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            body=await async_maybe_transform({"name": name}, broadcast_update_params.BroadcastUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastListResponse:
        """List broadcasts in your workspace.

        Cursor-paginated; returns broadcasts
        newest-first.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/broadcasts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    broadcast_list_params.BroadcastListParams,
                ),
            ),
            cast_to=BroadcastListResponse,
        )

    async def archive(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Archive a broadcast.

        This is a soft delete — the archived broadcast is returned
        and no longer appears in list results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._delete(
            path_template("/broadcasts/{broadcast_id}", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    async def cancel(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Cancel a broadcast's pending schedule, returning it to the draft state.

        Only
        valid for a scheduled broadcast.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._post(
            path_template("/broadcasts/{broadcast_id}/cancel", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    async def duplicate(
        self,
        broadcast_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """
        Duplicate a broadcast (and its template) into a new draft named "{source name}
        (copy)".

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._post(
            path_template("/broadcasts/{broadcast_id}/duplicate", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    async def put_content(
        self,
        broadcast_id: str,
        *,
        content: broadcast_put_content_params.Content,
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """
        Author the broadcast's content by replacing the draft elemental content of its
        private notification template. The draft is published automatically when the
        broadcast is sent or scheduled.

        Args:
          content: Elemental content payload. The server defaults `version` when omitted.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._put(
            path_template("/broadcasts/{broadcast_id}/content", broadcast_id=broadcast_id),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "state": state,
                },
                broadcast_put_content_params.BroadcastPutContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    async def retrieve_content(
        self,
        broadcast_id: str,
        *,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentGetResponse:
        """
        Retrieve the broadcast's content — the elemental content of its private
        notification template. Defaults to the working draft, since broadcast content is
        authored as a draft until the broadcast is sent.

        Args:
          version: Accepts `draft`, `published`, or a version string (e.g. `v001`). Defaults to
              `draft`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._get(
            path_template("/broadcasts/{broadcast_id}/content", broadcast_id=broadcast_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, broadcast_retrieve_content_params.BroadcastRetrieveContentParams
                ),
            ),
            cast_to=NotificationContentGetResponse,
        )

    async def schedule(
        self,
        broadcast_id: str,
        *,
        recipient_id: str,
        recipient_type: Literal["list", "audience"],
        scheduled_to: str,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Schedule a broadcast for a future send to a list or audience.

        Publishes the
        broadcast template first. Not allowed once the broadcast is sending or sent. For
        an immediate send use POST /broadcasts/{broadcastId}/send.

        Args:
          recipient_id: ID of the target list or audience.

          recipient_type: Whether the broadcast targets a list or an audience.

          scheduled_to: Wall-clock timestamp of the future send, no timezone offset (e.g.
              "2026-07-21T20:00:00"). The zone is given by `timezone`.

          timezone: IANA timezone for the scheduled send (e.g. America/New_York).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._post(
            path_template("/broadcasts/{broadcast_id}/schedule", broadcast_id=broadcast_id),
            body=await async_maybe_transform(
                {
                    "recipient_id": recipient_id,
                    "recipient_type": recipient_type,
                    "scheduled_to": scheduled_to,
                    "timezone": timezone,
                },
                broadcast_schedule_params.BroadcastScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )

    async def send(
        self,
        broadcast_id: str,
        *,
        recipient_id: str,
        recipient_type: Literal["list", "audience"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Broadcast:
        """Send a broadcast immediately to a list or audience.

        Publishes the broadcast
        template first. Not allowed once the broadcast is sending or sent.

        Args:
          recipient_id: ID of the target list or audience.

          recipient_type: Whether the broadcast targets a list or an audience.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not broadcast_id:
            raise ValueError(f"Expected a non-empty value for `broadcast_id` but received {broadcast_id!r}")
        return await self._post(
            path_template("/broadcasts/{broadcast_id}/send", broadcast_id=broadcast_id),
            body=await async_maybe_transform(
                {
                    "recipient_id": recipient_id,
                    "recipient_type": recipient_type,
                },
                broadcast_send_params.BroadcastSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Broadcast,
        )


class BroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = to_raw_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            broadcasts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            broadcasts.update,
        )
        self.list = to_raw_response_wrapper(
            broadcasts.list,
        )
        self.archive = to_raw_response_wrapper(
            broadcasts.archive,
        )
        self.cancel = to_raw_response_wrapper(
            broadcasts.cancel,
        )
        self.duplicate = to_raw_response_wrapper(
            broadcasts.duplicate,
        )
        self.put_content = to_raw_response_wrapper(
            broadcasts.put_content,
        )
        self.retrieve_content = to_raw_response_wrapper(
            broadcasts.retrieve_content,
        )
        self.schedule = to_raw_response_wrapper(
            broadcasts.schedule,
        )
        self.send = to_raw_response_wrapper(
            broadcasts.send,
        )


class AsyncBroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = async_to_raw_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            broadcasts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            broadcasts.update,
        )
        self.list = async_to_raw_response_wrapper(
            broadcasts.list,
        )
        self.archive = async_to_raw_response_wrapper(
            broadcasts.archive,
        )
        self.cancel = async_to_raw_response_wrapper(
            broadcasts.cancel,
        )
        self.duplicate = async_to_raw_response_wrapper(
            broadcasts.duplicate,
        )
        self.put_content = async_to_raw_response_wrapper(
            broadcasts.put_content,
        )
        self.retrieve_content = async_to_raw_response_wrapper(
            broadcasts.retrieve_content,
        )
        self.schedule = async_to_raw_response_wrapper(
            broadcasts.schedule,
        )
        self.send = async_to_raw_response_wrapper(
            broadcasts.send,
        )


class BroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = to_streamed_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            broadcasts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            broadcasts.update,
        )
        self.list = to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.archive = to_streamed_response_wrapper(
            broadcasts.archive,
        )
        self.cancel = to_streamed_response_wrapper(
            broadcasts.cancel,
        )
        self.duplicate = to_streamed_response_wrapper(
            broadcasts.duplicate,
        )
        self.put_content = to_streamed_response_wrapper(
            broadcasts.put_content,
        )
        self.retrieve_content = to_streamed_response_wrapper(
            broadcasts.retrieve_content,
        )
        self.schedule = to_streamed_response_wrapper(
            broadcasts.schedule,
        )
        self.send = to_streamed_response_wrapper(
            broadcasts.send,
        )


class AsyncBroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.create = async_to_streamed_response_wrapper(
            broadcasts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            broadcasts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            broadcasts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            broadcasts.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            broadcasts.archive,
        )
        self.cancel = async_to_streamed_response_wrapper(
            broadcasts.cancel,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            broadcasts.duplicate,
        )
        self.put_content = async_to_streamed_response_wrapper(
            broadcasts.put_content,
        )
        self.retrieve_content = async_to_streamed_response_wrapper(
            broadcasts.retrieve_content,
        )
        self.schedule = async_to_streamed_response_wrapper(
            broadcasts.schedule,
        )
        self.send = async_to_streamed_response_wrapper(
            broadcasts.send,
        )
