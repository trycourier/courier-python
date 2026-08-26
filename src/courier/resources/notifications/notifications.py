# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .checks import (
    ChecksResource,
    AsyncChecksResource,
    ChecksResourceWithRawResponse,
    AsyncChecksResourceWithRawResponse,
    ChecksResourceWithStreamingResponse,
    AsyncChecksResourceWithStreamingResponse,
)
from ...types import (
    NotificationTemplateState,
    notification_list_params,
    notification_create_params,
    notification_publish_params,
    notification_replace_params,
    notification_retrieve_params,
    notification_put_locale_params,
    notification_get_metrics_params,
    notification_put_content_params,
    notification_put_element_params,
    notification_list_versions_params,
    notification_retrieve_content_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.notification_list_response import NotificationListResponse
from ...types.notification_template_state import NotificationTemplateState
from ...types.notification_metrics_response import NotificationMetricsResponse
from ...types.notification_template_response import NotificationTemplateResponse
from ...types.notification_content_mutation_response import NotificationContentMutationResponse
from ...types.notification_retrieve_content_response import NotificationRetrieveContentResponse
from ...types.notification_template_write_payload_param import NotificationTemplateWritePayloadParam
from ...types.notification_template_version_list_response import NotificationTemplateVersionListResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    """
    Create, update, version, publish, and localize notification templates and their content.
    """

    @cached_property
    def checks(self) -> ChecksResource:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
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

    def create(
        self,
        *,
        notification: NotificationTemplateWritePayloadParam,
        state: Literal["DRAFT", "PUBLISHED"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateResponse:
        """Create a notification template.

        Requires all fields in the notification object.
        Templates are created in draft state by default.

        Args:
          notification: Template fields accepted in POST and PUT request bodies, nested under a
              `notification` key.

          state: Template state after creation. Case-insensitive input, normalized to uppercase
              in the response. Defaults to "DRAFT".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-idempotency-expiration": x_idempotency_expiration,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/notifications",
            body=maybe_transform(
                {
                    "notification": notification,
                    "state": state,
                },
                notification_create_params.NotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationTemplateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateResponse:
        """Retrieve a notification template by ID.

        Returns the published version by
        default. Pass version=draft to retrieve an unpublished template.

        Args:
          version: Version to retrieve. One of "draft", "published", or a version string like
              "v001". Defaults to "published".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/notifications/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, notification_retrieve_params.NotificationRetrieveParams),
            ),
            cast_to=NotificationTemplateResponse,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        event_id: str | Omit = omit,
        notes: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListResponse:
        """Lists the workspace's notification templates.

        Each carries a name, tags, brand,
        routing, and its draft or published state.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          event_id: Filter to templates linked to this event map ID.

          notes: Include template notes in the response. Only applies to legacy templates.

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
                        "event_id": event_id,
                        "notes": notes,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
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
        """Archives a notification template, preventing new sends from referencing it.

        The
        template stays retrievable for its version history.

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
            path_template("/notifications/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_metrics(
        self,
        id: str,
        *,
        end: Union[str, datetime] | Omit = omit,
        granularity: Literal["HOUR", "DAY", "WEEK", "MONTH"] | Omit = omit,
        lookback: str | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationMetricsResponse:
        """
        Fetch the delivery funnel for one Notification Template as a time series — sent,
        delivered, opened, clicked, errors, and undeliverable — broken out per provider
        and channel inside each bucket. Sum the entries in a bucket for its totals;
        there is no bucket-level total.

        Choose the window absolutely with `start` and `end`, or relatively with
        `lookback` (an ISO 8601 duration). `start` and `end` take precedence when both
        are supplied, and a request carrying neither defaults to `lookback=P30D`. The
        window is snapped outwards onto the `granularity` grid so every bucket it
        overlaps is returned whole, and the snapped boundaries come back as `start` and
        `end` — align a chart on those rather than on what was requested. Every boundary
        is UTC; there is no timezone support.

        Every bucket in the window is returned, including the quiet ones, whose `data`
        array is empty, so a series is directly plottable with no gap filling
        client-side. An unknown template id returns `200` with an all-empty series
        rather than `404`, and messages sent without a Notification Template never
        appear here.

        Available in the US region only.

        Args:
          end: The end of the window, as an ISO 8601 timestamp with an offset. Must be supplied
              together with `start`. An `end` in the future is accepted and not clamped — the
              trailing buckets come back empty.

          granularity: The size of each bucket in the series. Defaults to `DAY`. `WEEK` buckets start
              on Sunday. A fine granularity caps the window it can cover: `HOUR` spans at most
              7 days and `DAY` at most 90 days, and a wider window returns `400` — request a
              coarser granularity instead. `WEEK` and `MONTH` are uncapped, subject to the
              1000-bucket limit on a single response.

          lookback: The length of the window, counted back from now, as an ISO 8601 duration
              (`P30D`, `P12W`, `PT12H`). Defaults to `P30D`, and is ignored when `start` and
              `end` are supplied. A malformed or non-positive duration returns `400`.

          start: The inclusive start of the window, as an ISO 8601 timestamp with an offset
              (`2026-04-01T00:00:00Z`). Must be supplied together with `end` and be earlier
              than it; either one alone returns `400`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/notifications/{id}/metrics", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "granularity": granularity,
                        "lookback": lookback,
                        "start": start,
                    },
                    notification_get_metrics_params.NotificationGetMetricsParams,
                ),
            ),
            cast_to=NotificationMetricsResponse,
        )

    def list_versions(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateVersionListResponse:
        """
        Returns a notification template's published versions, most recent first, for
        comparison or rollback. Paged.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of versions to return per page. Default 10, max 10.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/notifications/{id}/versions", id=id),
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
                    notification_list_versions_params.NotificationListVersionsParams,
                ),
            ),
            cast_to=NotificationTemplateVersionListResponse,
        )

    def publish(
        self,
        id: str,
        *,
        version: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Publish a notification template.

        Publishes the current draft by default. Pass a
        version in the request body to publish a specific historical version.

        Args:
          version: Historical version to publish (e.g. "v001"). Omit to publish the current draft.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-idempotency-expiration": x_idempotency_expiration,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/notifications/{id}/publish", id=id),
            body=maybe_transform({"version": version}, notification_publish_params.NotificationPublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def put_content(
        self,
        id: str,
        *,
        content: notification_put_content_params.Content,
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """Replaces all Elemental content in a template, overwriting every existing
        element.

        Supported for V2 templates only, not V1 blocks and channels.

        Args:
          content: Elemental content payload. The server defaults `version` when omitted.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/notifications/{id}/content", id=id),
            body=maybe_transform(
                {
                    "content": content,
                    "state": state,
                },
                notification_put_content_params.NotificationPutContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    def put_element(
        self,
        element_id: str,
        *,
        id: str,
        type: str,
        channels: SequenceNotStr[str] | Omit = omit,
        data: Dict[str, object] | Omit = omit,
        if_: str | Omit = omit,
        loop: str | Omit = omit,
        ref: str | Omit = omit,
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """
        Replaces one Elemental element in a template, addressed by its element id.
        Supported for V2 templates only, not V1 blocks and channels.

        Args:
          type: Element type (text, meta, action, image, etc.).

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not element_id:
            raise ValueError(f"Expected a non-empty value for `element_id` but received {element_id!r}")
        return self._put(
            path_template("/notifications/{id}/elements/{element_id}", id=id, element_id=element_id),
            body=maybe_transform(
                {
                    "type": type,
                    "channels": channels,
                    "data": data,
                    "if_": if_,
                    "loop": loop,
                    "ref": ref,
                    "state": state,
                },
                notification_put_element_params.NotificationPutElementParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    def put_locale(
        self,
        locale_id: str,
        *,
        id: str,
        elements: Iterable[notification_put_locale_params.Element],
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """Sets locale-specific content overrides for a template.

        Each override must
        reference an element that already exists in the default content.

        Args:
          elements: Elements with locale-specific content overrides.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not locale_id:
            raise ValueError(f"Expected a non-empty value for `locale_id` but received {locale_id!r}")
        return self._put(
            path_template("/notifications/{id}/locales/{locale_id}", id=id, locale_id=locale_id),
            body=maybe_transform(
                {
                    "elements": elements,
                    "state": state,
                },
                notification_put_locale_params.NotificationPutLocaleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    def replace(
        self,
        id: str,
        *,
        notification: NotificationTemplateWritePayloadParam,
        state: Literal["DRAFT", "PUBLISHED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateResponse:
        """
        Replaces a notification template in full, so send every field rather than only
        the ones you want changed. Publish separately to make it live.

        Args:
          notification: Template fields accepted in POST and PUT request bodies, nested under a
              `notification` key.

          state: Template state after update. Case-insensitive input, normalized to uppercase in
              the response. Defaults to "DRAFT".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/notifications/{id}", id=id),
            body=maybe_transform(
                {
                    "notification": notification,
                    "state": state,
                },
                notification_replace_params.NotificationReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationTemplateResponse,
        )

    def retrieve_content(
        self,
        id: str,
        *,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationRetrieveContentResponse:
        """Returns a template's content and checksum.

        V2 templates return Elemental
        elements, while V1 templates return blocks and channels instead.

        Args:
          version: Accepts `draft`, `published`, or a version string (e.g., `v001`). Defaults to
              `published`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            NotificationRetrieveContentResponse,
            self._get(
                path_template("/notifications/{id}/content", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"version": version}, notification_retrieve_content_params.NotificationRetrieveContentParams
                    ),
                ),
                cast_to=cast(
                    Any, NotificationRetrieveContentResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncNotificationsResource(AsyncAPIResource):
    """
    Create, update, version, publish, and localize notification templates and their content.
    """

    @cached_property
    def checks(self) -> AsyncChecksResource:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
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

    async def create(
        self,
        *,
        notification: NotificationTemplateWritePayloadParam,
        state: Literal["DRAFT", "PUBLISHED"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateResponse:
        """Create a notification template.

        Requires all fields in the notification object.
        Templates are created in draft state by default.

        Args:
          notification: Template fields accepted in POST and PUT request bodies, nested under a
              `notification` key.

          state: Template state after creation. Case-insensitive input, normalized to uppercase
              in the response. Defaults to "DRAFT".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-idempotency-expiration": x_idempotency_expiration,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/notifications",
            body=await async_maybe_transform(
                {
                    "notification": notification,
                    "state": state,
                },
                notification_create_params.NotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationTemplateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateResponse:
        """Retrieve a notification template by ID.

        Returns the published version by
        default. Pass version=draft to retrieve an unpublished template.

        Args:
          version: Version to retrieve. One of "draft", "published", or a version string like
              "v001". Defaults to "published".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/notifications/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, notification_retrieve_params.NotificationRetrieveParams
                ),
            ),
            cast_to=NotificationTemplateResponse,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        event_id: str | Omit = omit,
        notes: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListResponse:
        """Lists the workspace's notification templates.

        Each carries a name, tags, brand,
        routing, and its draft or published state.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          event_id: Filter to templates linked to this event map ID.

          notes: Include template notes in the response. Only applies to legacy templates.

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
                        "event_id": event_id,
                        "notes": notes,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
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
        """Archives a notification template, preventing new sends from referencing it.

        The
        template stays retrievable for its version history.

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
            path_template("/notifications/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_metrics(
        self,
        id: str,
        *,
        end: Union[str, datetime] | Omit = omit,
        granularity: Literal["HOUR", "DAY", "WEEK", "MONTH"] | Omit = omit,
        lookback: str | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationMetricsResponse:
        """
        Fetch the delivery funnel for one Notification Template as a time series — sent,
        delivered, opened, clicked, errors, and undeliverable — broken out per provider
        and channel inside each bucket. Sum the entries in a bucket for its totals;
        there is no bucket-level total.

        Choose the window absolutely with `start` and `end`, or relatively with
        `lookback` (an ISO 8601 duration). `start` and `end` take precedence when both
        are supplied, and a request carrying neither defaults to `lookback=P30D`. The
        window is snapped outwards onto the `granularity` grid so every bucket it
        overlaps is returned whole, and the snapped boundaries come back as `start` and
        `end` — align a chart on those rather than on what was requested. Every boundary
        is UTC; there is no timezone support.

        Every bucket in the window is returned, including the quiet ones, whose `data`
        array is empty, so a series is directly plottable with no gap filling
        client-side. An unknown template id returns `200` with an all-empty series
        rather than `404`, and messages sent without a Notification Template never
        appear here.

        Available in the US region only.

        Args:
          end: The end of the window, as an ISO 8601 timestamp with an offset. Must be supplied
              together with `start`. An `end` in the future is accepted and not clamped — the
              trailing buckets come back empty.

          granularity: The size of each bucket in the series. Defaults to `DAY`. `WEEK` buckets start
              on Sunday. A fine granularity caps the window it can cover: `HOUR` spans at most
              7 days and `DAY` at most 90 days, and a wider window returns `400` — request a
              coarser granularity instead. `WEEK` and `MONTH` are uncapped, subject to the
              1000-bucket limit on a single response.

          lookback: The length of the window, counted back from now, as an ISO 8601 duration
              (`P30D`, `P12W`, `PT12H`). Defaults to `P30D`, and is ignored when `start` and
              `end` are supplied. A malformed or non-positive duration returns `400`.

          start: The inclusive start of the window, as an ISO 8601 timestamp with an offset
              (`2026-04-01T00:00:00Z`). Must be supplied together with `end` and be earlier
              than it; either one alone returns `400`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/notifications/{id}/metrics", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "granularity": granularity,
                        "lookback": lookback,
                        "start": start,
                    },
                    notification_get_metrics_params.NotificationGetMetricsParams,
                ),
            ),
            cast_to=NotificationMetricsResponse,
        )

    async def list_versions(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateVersionListResponse:
        """
        Returns a notification template's published versions, most recent first, for
        comparison or rollback. Paged.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of versions to return per page. Default 10, max 10.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/notifications/{id}/versions", id=id),
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
                    notification_list_versions_params.NotificationListVersionsParams,
                ),
            ),
            cast_to=NotificationTemplateVersionListResponse,
        )

    async def publish(
        self,
        id: str,
        *,
        version: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Publish a notification template.

        Publishes the current draft by default. Pass a
        version in the request body to publish a specific historical version.

        Args:
          version: Historical version to publish (e.g. "v001"). Omit to publish the current draft.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-idempotency-expiration": x_idempotency_expiration,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/notifications/{id}/publish", id=id),
            body=await async_maybe_transform(
                {"version": version}, notification_publish_params.NotificationPublishParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def put_content(
        self,
        id: str,
        *,
        content: notification_put_content_params.Content,
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """Replaces all Elemental content in a template, overwriting every existing
        element.

        Supported for V2 templates only, not V1 blocks and channels.

        Args:
          content: Elemental content payload. The server defaults `version` when omitted.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/notifications/{id}/content", id=id),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "state": state,
                },
                notification_put_content_params.NotificationPutContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    async def put_element(
        self,
        element_id: str,
        *,
        id: str,
        type: str,
        channels: SequenceNotStr[str] | Omit = omit,
        data: Dict[str, object] | Omit = omit,
        if_: str | Omit = omit,
        loop: str | Omit = omit,
        ref: str | Omit = omit,
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """
        Replaces one Elemental element in a template, addressed by its element id.
        Supported for V2 templates only, not V1 blocks and channels.

        Args:
          type: Element type (text, meta, action, image, etc.).

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not element_id:
            raise ValueError(f"Expected a non-empty value for `element_id` but received {element_id!r}")
        return await self._put(
            path_template("/notifications/{id}/elements/{element_id}", id=id, element_id=element_id),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "channels": channels,
                    "data": data,
                    "if_": if_,
                    "loop": loop,
                    "ref": ref,
                    "state": state,
                },
                notification_put_element_params.NotificationPutElementParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    async def put_locale(
        self,
        locale_id: str,
        *,
        id: str,
        elements: Iterable[notification_put_locale_params.Element],
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """Sets locale-specific content overrides for a template.

        Each override must
        reference an element that already exists in the default content.

        Args:
          elements: Elements with locale-specific content overrides.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not locale_id:
            raise ValueError(f"Expected a non-empty value for `locale_id` but received {locale_id!r}")
        return await self._put(
            path_template("/notifications/{id}/locales/{locale_id}", id=id, locale_id=locale_id),
            body=await async_maybe_transform(
                {
                    "elements": elements,
                    "state": state,
                },
                notification_put_locale_params.NotificationPutLocaleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    async def replace(
        self,
        id: str,
        *,
        notification: NotificationTemplateWritePayloadParam,
        state: Literal["DRAFT", "PUBLISHED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateResponse:
        """
        Replaces a notification template in full, so send every field rather than only
        the ones you want changed. Publish separately to make it live.

        Args:
          notification: Template fields accepted in POST and PUT request bodies, nested under a
              `notification` key.

          state: Template state after update. Case-insensitive input, normalized to uppercase in
              the response. Defaults to "DRAFT".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/notifications/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "notification": notification,
                    "state": state,
                },
                notification_replace_params.NotificationReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationTemplateResponse,
        )

    async def retrieve_content(
        self,
        id: str,
        *,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationRetrieveContentResponse:
        """Returns a template's content and checksum.

        V2 templates return Elemental
        elements, while V1 templates return blocks and channels instead.

        Args:
          version: Accepts `draft`, `published`, or a version string (e.g., `v001`). Defaults to
              `published`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            NotificationRetrieveContentResponse,
            await self._get(
                path_template("/notifications/{id}/content", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"version": version}, notification_retrieve_content_params.NotificationRetrieveContentParams
                    ),
                ),
                cast_to=cast(
                    Any, NotificationRetrieveContentResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.list = to_raw_response_wrapper(
            notifications.list,
        )
        self.archive = to_raw_response_wrapper(
            notifications.archive,
        )
        self.get_metrics = to_raw_response_wrapper(
            notifications.get_metrics,
        )
        self.list_versions = to_raw_response_wrapper(
            notifications.list_versions,
        )
        self.publish = to_raw_response_wrapper(
            notifications.publish,
        )
        self.put_content = to_raw_response_wrapper(
            notifications.put_content,
        )
        self.put_element = to_raw_response_wrapper(
            notifications.put_element,
        )
        self.put_locale = to_raw_response_wrapper(
            notifications.put_locale,
        )
        self.replace = to_raw_response_wrapper(
            notifications.replace,
        )
        self.retrieve_content = to_raw_response_wrapper(
            notifications.retrieve_content,
        )

    @cached_property
    def checks(self) -> ChecksResourceWithRawResponse:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        return ChecksResourceWithRawResponse(self._notifications.checks)


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            notifications.list,
        )
        self.archive = async_to_raw_response_wrapper(
            notifications.archive,
        )
        self.get_metrics = async_to_raw_response_wrapper(
            notifications.get_metrics,
        )
        self.list_versions = async_to_raw_response_wrapper(
            notifications.list_versions,
        )
        self.publish = async_to_raw_response_wrapper(
            notifications.publish,
        )
        self.put_content = async_to_raw_response_wrapper(
            notifications.put_content,
        )
        self.put_element = async_to_raw_response_wrapper(
            notifications.put_element,
        )
        self.put_locale = async_to_raw_response_wrapper(
            notifications.put_locale,
        )
        self.replace = async_to_raw_response_wrapper(
            notifications.replace,
        )
        self.retrieve_content = async_to_raw_response_wrapper(
            notifications.retrieve_content,
        )

    @cached_property
    def checks(self) -> AsyncChecksResourceWithRawResponse:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        return AsyncChecksResourceWithRawResponse(self._notifications.checks)


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            notifications.list,
        )
        self.archive = to_streamed_response_wrapper(
            notifications.archive,
        )
        self.get_metrics = to_streamed_response_wrapper(
            notifications.get_metrics,
        )
        self.list_versions = to_streamed_response_wrapper(
            notifications.list_versions,
        )
        self.publish = to_streamed_response_wrapper(
            notifications.publish,
        )
        self.put_content = to_streamed_response_wrapper(
            notifications.put_content,
        )
        self.put_element = to_streamed_response_wrapper(
            notifications.put_element,
        )
        self.put_locale = to_streamed_response_wrapper(
            notifications.put_locale,
        )
        self.replace = to_streamed_response_wrapper(
            notifications.replace,
        )
        self.retrieve_content = to_streamed_response_wrapper(
            notifications.retrieve_content,
        )

    @cached_property
    def checks(self) -> ChecksResourceWithStreamingResponse:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        return ChecksResourceWithStreamingResponse(self._notifications.checks)


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            notifications.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            notifications.archive,
        )
        self.get_metrics = async_to_streamed_response_wrapper(
            notifications.get_metrics,
        )
        self.list_versions = async_to_streamed_response_wrapper(
            notifications.list_versions,
        )
        self.publish = async_to_streamed_response_wrapper(
            notifications.publish,
        )
        self.put_content = async_to_streamed_response_wrapper(
            notifications.put_content,
        )
        self.put_element = async_to_streamed_response_wrapper(
            notifications.put_element,
        )
        self.put_locale = async_to_streamed_response_wrapper(
            notifications.put_locale,
        )
        self.replace = async_to_streamed_response_wrapper(
            notifications.replace,
        )
        self.retrieve_content = async_to_streamed_response_wrapper(
            notifications.retrieve_content,
        )

    @cached_property
    def checks(self) -> AsyncChecksResourceWithStreamingResponse:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        return AsyncChecksResourceWithStreamingResponse(self._notifications.checks)
