# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    routing_strategy_list_params,
    routing_strategy_create_params,
    routing_strategy_replace_params,
    routing_strategy_list_notifications_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.routing_strategy_get_response import RoutingStrategyGetResponse
from ..types.shared_params.message_routing import MessageRouting
from ..types.routing_strategy_list_response import RoutingStrategyListResponse
from ..types.shared_params.message_channels import MessageChannels
from ..types.shared_params.message_providers import MessageProviders
from ..types.associated_notification_list_response import AssociatedNotificationListResponse

__all__ = ["RoutingStrategiesResource", "AsyncRoutingStrategiesResource"]


class RoutingStrategiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutingStrategiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return RoutingStrategiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingStrategiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return RoutingStrategiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        routing: MessageRouting,
        channels: Optional[MessageChannels] | Omit = omit,
        description: Optional[str] | Omit = omit,
        providers: Optional[MessageProviders] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingStrategyGetResponse:
        """Create a routing strategy.

        Requires a name and routing configuration at minimum.
        Channels and providers default to empty if omitted.

        Args:
          name: Human-readable name for the routing strategy.

          routing: Routing tree defining channel selection method and order.

          channels: Per-channel delivery configuration. Defaults to empty if omitted.

          description: Optional description of the routing strategy.

          providers: Per-provider delivery configuration. Defaults to empty if omitted.

          tags: Optional tags for categorization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/routing-strategies",
            body=maybe_transform(
                {
                    "name": name,
                    "routing": routing,
                    "channels": channels,
                    "description": description,
                    "providers": providers,
                    "tags": tags,
                },
                routing_strategy_create_params.RoutingStrategyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingStrategyGetResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingStrategyGetResponse:
        """Retrieve a routing strategy by ID.

        Returns the full entity including routing
        content and metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/routing-strategies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingStrategyGetResponse,
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
    ) -> RoutingStrategyListResponse:
        """List routing strategies in your workspace.

        Returns metadata only (no
        routing/channels/providers content). Use GET /routing-strategies/{id} for full
        details.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of results per page. Default 20, max 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/routing-strategies",
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
                    routing_strategy_list_params.RoutingStrategyListParams,
                ),
            ),
            cast_to=RoutingStrategyListResponse,
        )

    def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive a routing strategy.

        The strategy must not have associated notification
        templates. Unlink all templates before archiving.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/routing-strategies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_notifications(
        self,
        id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssociatedNotificationListResponse:
        """List notification templates associated with a routing strategy.

        Includes
        template metadata only, not full content.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of results per page. Default 20, max 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/routing-strategies/{id}/notifications", id=id),
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
                    routing_strategy_list_notifications_params.RoutingStrategyListNotificationsParams,
                ),
            ),
            cast_to=AssociatedNotificationListResponse,
        )

    def replace(
        self,
        id: str,
        *,
        name: str,
        routing: MessageRouting,
        channels: Optional[MessageChannels] | Omit = omit,
        description: Optional[str] | Omit = omit,
        providers: Optional[MessageProviders] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingStrategyGetResponse:
        """Replace a routing strategy.

        Full document replacement; the caller must send the
        complete desired state. Missing optional fields are cleared.

        Args:
          name: Human-readable name for the routing strategy.

          routing: Routing tree defining channel selection method and order.

          channels: Per-channel delivery configuration. Omit to clear.

          description: Optional description. Omit or null to clear.

          providers: Per-provider delivery configuration. Omit to clear.

          tags: Optional tags. Omit or null to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/routing-strategies/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "routing": routing,
                    "channels": channels,
                    "description": description,
                    "providers": providers,
                    "tags": tags,
                },
                routing_strategy_replace_params.RoutingStrategyReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingStrategyGetResponse,
        )


class AsyncRoutingStrategiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutingStrategiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutingStrategiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingStrategiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncRoutingStrategiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        routing: MessageRouting,
        channels: Optional[MessageChannels] | Omit = omit,
        description: Optional[str] | Omit = omit,
        providers: Optional[MessageProviders] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingStrategyGetResponse:
        """Create a routing strategy.

        Requires a name and routing configuration at minimum.
        Channels and providers default to empty if omitted.

        Args:
          name: Human-readable name for the routing strategy.

          routing: Routing tree defining channel selection method and order.

          channels: Per-channel delivery configuration. Defaults to empty if omitted.

          description: Optional description of the routing strategy.

          providers: Per-provider delivery configuration. Defaults to empty if omitted.

          tags: Optional tags for categorization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/routing-strategies",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "routing": routing,
                    "channels": channels,
                    "description": description,
                    "providers": providers,
                    "tags": tags,
                },
                routing_strategy_create_params.RoutingStrategyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingStrategyGetResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingStrategyGetResponse:
        """Retrieve a routing strategy by ID.

        Returns the full entity including routing
        content and metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/routing-strategies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingStrategyGetResponse,
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
    ) -> RoutingStrategyListResponse:
        """List routing strategies in your workspace.

        Returns metadata only (no
        routing/channels/providers content). Use GET /routing-strategies/{id} for full
        details.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of results per page. Default 20, max 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/routing-strategies",
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
                    routing_strategy_list_params.RoutingStrategyListParams,
                ),
            ),
            cast_to=RoutingStrategyListResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive a routing strategy.

        The strategy must not have associated notification
        templates. Unlink all templates before archiving.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/routing-strategies/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_notifications(
        self,
        id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssociatedNotificationListResponse:
        """List notification templates associated with a routing strategy.

        Includes
        template metadata only, not full content.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of results per page. Default 20, max 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/routing-strategies/{id}/notifications", id=id),
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
                    routing_strategy_list_notifications_params.RoutingStrategyListNotificationsParams,
                ),
            ),
            cast_to=AssociatedNotificationListResponse,
        )

    async def replace(
        self,
        id: str,
        *,
        name: str,
        routing: MessageRouting,
        channels: Optional[MessageChannels] | Omit = omit,
        description: Optional[str] | Omit = omit,
        providers: Optional[MessageProviders] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingStrategyGetResponse:
        """Replace a routing strategy.

        Full document replacement; the caller must send the
        complete desired state. Missing optional fields are cleared.

        Args:
          name: Human-readable name for the routing strategy.

          routing: Routing tree defining channel selection method and order.

          channels: Per-channel delivery configuration. Omit to clear.

          description: Optional description. Omit or null to clear.

          providers: Per-provider delivery configuration. Omit to clear.

          tags: Optional tags. Omit or null to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/routing-strategies/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "routing": routing,
                    "channels": channels,
                    "description": description,
                    "providers": providers,
                    "tags": tags,
                },
                routing_strategy_replace_params.RoutingStrategyReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingStrategyGetResponse,
        )


class RoutingStrategiesResourceWithRawResponse:
    def __init__(self, routing_strategies: RoutingStrategiesResource) -> None:
        self._routing_strategies = routing_strategies

        self.create = to_raw_response_wrapper(
            routing_strategies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            routing_strategies.retrieve,
        )
        self.list = to_raw_response_wrapper(
            routing_strategies.list,
        )
        self.archive = to_raw_response_wrapper(
            routing_strategies.archive,
        )
        self.list_notifications = to_raw_response_wrapper(
            routing_strategies.list_notifications,
        )
        self.replace = to_raw_response_wrapper(
            routing_strategies.replace,
        )


class AsyncRoutingStrategiesResourceWithRawResponse:
    def __init__(self, routing_strategies: AsyncRoutingStrategiesResource) -> None:
        self._routing_strategies = routing_strategies

        self.create = async_to_raw_response_wrapper(
            routing_strategies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            routing_strategies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            routing_strategies.list,
        )
        self.archive = async_to_raw_response_wrapper(
            routing_strategies.archive,
        )
        self.list_notifications = async_to_raw_response_wrapper(
            routing_strategies.list_notifications,
        )
        self.replace = async_to_raw_response_wrapper(
            routing_strategies.replace,
        )


class RoutingStrategiesResourceWithStreamingResponse:
    def __init__(self, routing_strategies: RoutingStrategiesResource) -> None:
        self._routing_strategies = routing_strategies

        self.create = to_streamed_response_wrapper(
            routing_strategies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            routing_strategies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            routing_strategies.list,
        )
        self.archive = to_streamed_response_wrapper(
            routing_strategies.archive,
        )
        self.list_notifications = to_streamed_response_wrapper(
            routing_strategies.list_notifications,
        )
        self.replace = to_streamed_response_wrapper(
            routing_strategies.replace,
        )


class AsyncRoutingStrategiesResourceWithStreamingResponse:
    def __init__(self, routing_strategies: AsyncRoutingStrategiesResource) -> None:
        self._routing_strategies = routing_strategies

        self.create = async_to_streamed_response_wrapper(
            routing_strategies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            routing_strategies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            routing_strategies.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            routing_strategies.archive,
        )
        self.list_notifications = async_to_streamed_response_wrapper(
            routing_strategies.list_notifications,
        )
        self.replace = async_to_streamed_response_wrapper(
            routing_strategies.replace,
        )
