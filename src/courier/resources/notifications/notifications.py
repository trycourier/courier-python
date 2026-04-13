# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Iterable, Optional, cast
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
    notification_put_content_params,
    notification_put_element_params,
    notification_list_versions_params,
    notification_retrieve_content_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.notification_template_get_response import NotificationTemplateGetResponse
from ...types.notification_template_payload_param import NotificationTemplatePayloadParam
from ...types.notification_content_mutation_response import NotificationContentMutationResponse
from ...types.notification_retrieve_content_response import NotificationRetrieveContentResponse
from ...types.notification_template_version_list_response import NotificationTemplateVersionListResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
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

    def create(
        self,
        *,
        notification: NotificationTemplatePayloadParam,
        state: Literal["DRAFT", "PUBLISHED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateGetResponse:
        """Create a notification template.

        Requires all fields in the notification object.
        Templates are created in draft state by default.

        Args:
          notification: Full document shape used in POST and PUT request bodies, and returned inside the
              GET response envelope.

          state: Template state after creation. Case-insensitive input, normalized to uppercase
              in the response. Defaults to "DRAFT".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            cast_to=NotificationTemplateGetResponse,
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
    ) -> NotificationTemplateGetResponse:
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
            cast_to=NotificationTemplateGetResponse,
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
        """
        List notification templates in your workspace.

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
        """
        Archive a notification template.

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
        List versions of a notification template.

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
        """Replace the elemental content of a notification template.

        Overwrites all
        elements in the template with the provided content. Only supported for V2
        (elemental) templates.

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
        """Update a single element within a notification template.

        Only supported for V2
        (elemental) templates.

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
        """Set locale-specific content overrides for a notification template.

        Each element
        override must reference an existing element by ID. Only supported for V2
        (elemental) templates.

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
        notification: NotificationTemplatePayloadParam,
        state: Literal["DRAFT", "PUBLISHED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateGetResponse:
        """Replace a notification template.

        All fields are required.

        Args:
          notification: Full document shape used in POST and PUT request bodies, and returned inside the
              GET response envelope.

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
            cast_to=NotificationTemplateGetResponse,
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
        """Retrieve the content of a notification template.

        The response shape depends on
        whether the template uses V1 (blocks/channels) or V2 (elemental) content. Use
        the `version` query parameter to select draft, published, or a specific
        historical version.

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

    async def create(
        self,
        *,
        notification: NotificationTemplatePayloadParam,
        state: Literal["DRAFT", "PUBLISHED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateGetResponse:
        """Create a notification template.

        Requires all fields in the notification object.
        Templates are created in draft state by default.

        Args:
          notification: Full document shape used in POST and PUT request bodies, and returned inside the
              GET response envelope.

          state: Template state after creation. Case-insensitive input, normalized to uppercase
              in the response. Defaults to "DRAFT".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            cast_to=NotificationTemplateGetResponse,
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
    ) -> NotificationTemplateGetResponse:
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
            cast_to=NotificationTemplateGetResponse,
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
        """
        List notification templates in your workspace.

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
        """
        Archive a notification template.

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
        List versions of a notification template.

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
        """Replace the elemental content of a notification template.

        Overwrites all
        elements in the template with the provided content. Only supported for V2
        (elemental) templates.

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
        """Update a single element within a notification template.

        Only supported for V2
        (elemental) templates.

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
        """Set locale-specific content overrides for a notification template.

        Each element
        override must reference an existing element by ID. Only supported for V2
        (elemental) templates.

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
        notification: NotificationTemplatePayloadParam,
        state: Literal["DRAFT", "PUBLISHED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateGetResponse:
        """Replace a notification template.

        All fields are required.

        Args:
          notification: Full document shape used in POST and PUT request bodies, and returned inside the
              GET response envelope.

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
            cast_to=NotificationTemplateGetResponse,
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
        """Retrieve the content of a notification template.

        The response shape depends on
        whether the template uses V1 (blocks/channels) or V2 (elemental) content. Use
        the `version` query parameter to select draft, published, or a specific
        historical version.

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
        return AsyncChecksResourceWithStreamingResponse(self._notifications.checks)
