# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...types import NotificationTemplateState
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.journeys import (
    template_list_params,
    template_create_params,
    template_publish_params,
    template_replace_params,
    template_put_locale_params,
    template_put_content_params,
    template_retrieve_content_params,
)
from ...types.notification_template_state import NotificationTemplateState
from ...types.journey_template_get_response import JourneyTemplateGetResponse
from ...types.journey_template_list_response import JourneyTemplateListResponse
from ...types.notification_content_get_response import NotificationContentGetResponse
from ...types.notification_content_mutation_response import NotificationContentMutationResponse
from ...types.notification_template_version_list_response import NotificationTemplateVersionListResponse

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    """
    Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
    """

    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return TemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        template_id: str,
        *,
        channel: str,
        notification: template_create_params.Notification,
        provider_key: str | Omit = omit,
        state: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyTemplateGetResponse:
        """Create a notification template scoped to this journey.

        Defaults to `DRAFT`
        state; pass `state: "PUBLISHED"` to publish on create.

        The content tree must contain exactly one channel block whose `channel` matches
        the `channel` on the request — a journey-scoped template carries a single
        channel. Top-level elements, or a block for a different channel, return `400`.
        The template designer renders only the channel block matching the tab it draws,
        so content stored without one cannot be opened. An empty `elements` array is
        accepted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
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
            path_template("/journeys/{template_id}/templates", template_id=template_id),
            body=maybe_transform(
                {
                    "channel": channel,
                    "notification": notification,
                    "provider_key": provider_key,
                    "state": state,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyTemplateGetResponse,
        )

    def retrieve(
        self,
        notification_id: str,
        *,
        template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyTemplateGetResponse:
        """
        Returns a journey's own notification template with its name, brand, subscription
        topic, and content. Defaults to the published version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return self._get(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}",
                template_id=template_id,
                notification_id=notification_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyTemplateGetResponse,
        )

    def list(
        self,
        template_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyTemplateListResponse:
        """List notification templates scoped to this journey.

        Journey-scoped notification
        templates can only be referenced from `send` nodes within the same journey.

        Args:
          cursor: Pagination cursor from a prior response.

          limit: Page size. Minimum 1, maximum 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._get(
            path_template("/journeys/{template_id}/templates", template_id=template_id),
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
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=JourneyTemplateListResponse,
        )

    def archive(
        self,
        notification_id: str,
        *,
        template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archives one journey's notification template, preventing further sends.

        Detach
        any send node referencing it beforehand.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}",
                template_id=template_id,
                notification_id=notification_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_versions(
        self,
        notification_id: str,
        *,
        template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateVersionListResponse:
        """
        Lists the published versions of a template that belongs to a journey, most
        recent first. Paged by cursor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return self._get(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/versions",
                template_id=template_id,
                notification_id=notification_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationTemplateVersionListResponse,
        )

    def publish(
        self,
        notification_id: str,
        *,
        template_id: str,
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
        """Publishes a journey-scoped template's draft as a new version.

        Pass a version
        instead to roll back the template to an earlier publish.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
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
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/publish",
                template_id=template_id,
                notification_id=notification_id,
            ),
            body=maybe_transform({"version": version}, template_publish_params.TemplatePublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def put_content(
        self,
        notification_id: str,
        *,
        template_id: str,
        content: template_put_content_params.Content,
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """
        Replace the elemental content of a journey-scoped notification template.
        Overwrites all elements in the template draft with the provided content.

        Args:
          content: Elemental content payload. The server defaults `version` when omitted.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return self._put(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/content",
                template_id=template_id,
                notification_id=notification_id,
            ),
            body=maybe_transform(
                {
                    "content": content,
                    "state": state,
                },
                template_put_content_params.TemplatePutContentParams,
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
        template_id: str,
        notification_id: str,
        elements: Iterable[template_put_locale_params.Element],
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """Set locale-specific content overrides for a journey-scoped notification
        template.

        Each element override must reference an existing element by ID.

        Args:
          elements: Elements with locale-specific content overrides.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        if not locale_id:
            raise ValueError(f"Expected a non-empty value for `locale_id` but received {locale_id!r}")
        return self._put(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/locales/{locale_id}",
                template_id=template_id,
                notification_id=notification_id,
                locale_id=locale_id,
            ),
            body=maybe_transform(
                {
                    "elements": elements,
                    "state": state,
                },
                template_put_locale_params.TemplatePutLocaleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    def replace(
        self,
        notification_id: str,
        *,
        template_id: str,
        notification: template_replace_params.Notification,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyTemplateGetResponse:
        """Replaces the draft content of one journey's notification template.

        Publish it
        before send nodes referencing it render the change.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return self._put(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}",
                template_id=template_id,
                notification_id=notification_id,
            ),
            body=maybe_transform(
                {
                    "notification": notification,
                    "state": state,
                },
                template_replace_params.TemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyTemplateGetResponse,
        )

    def retrieve_content(
        self,
        notification_id: str,
        *,
        template_id: str,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentGetResponse:
        """
        Returns the Elemental elements and version of a journey-scoped template's
        content. Compare versions to see what changed between publishes.

        Args:
          version: Accepts `draft`, `published`, or a version string (e.g., `v001`). Defaults to
              `published`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return self._get(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/content",
                template_id=template_id,
                notification_id=notification_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"version": version}, template_retrieve_content_params.TemplateRetrieveContentParams
                ),
            ),
            cast_to=NotificationContentGetResponse,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    """
    Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        template_id: str,
        *,
        channel: str,
        notification: template_create_params.Notification,
        provider_key: str | Omit = omit,
        state: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyTemplateGetResponse:
        """Create a notification template scoped to this journey.

        Defaults to `DRAFT`
        state; pass `state: "PUBLISHED"` to publish on create.

        The content tree must contain exactly one channel block whose `channel` matches
        the `channel` on the request — a journey-scoped template carries a single
        channel. Top-level elements, or a block for a different channel, return `400`.
        The template designer renders only the channel block matching the tab it draws,
        so content stored without one cannot be opened. An empty `elements` array is
        accepted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
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
            path_template("/journeys/{template_id}/templates", template_id=template_id),
            body=await async_maybe_transform(
                {
                    "channel": channel,
                    "notification": notification,
                    "provider_key": provider_key,
                    "state": state,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyTemplateGetResponse,
        )

    async def retrieve(
        self,
        notification_id: str,
        *,
        template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyTemplateGetResponse:
        """
        Returns a journey's own notification template with its name, brand, subscription
        topic, and content. Defaults to the published version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return await self._get(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}",
                template_id=template_id,
                notification_id=notification_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyTemplateGetResponse,
        )

    async def list(
        self,
        template_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyTemplateListResponse:
        """List notification templates scoped to this journey.

        Journey-scoped notification
        templates can only be referenced from `send` nodes within the same journey.

        Args:
          cursor: Pagination cursor from a prior response.

          limit: Page size. Minimum 1, maximum 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._get(
            path_template("/journeys/{template_id}/templates", template_id=template_id),
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
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=JourneyTemplateListResponse,
        )

    async def archive(
        self,
        notification_id: str,
        *,
        template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archives one journey's notification template, preventing further sends.

        Detach
        any send node referencing it beforehand.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}",
                template_id=template_id,
                notification_id=notification_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_versions(
        self,
        notification_id: str,
        *,
        template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationTemplateVersionListResponse:
        """
        Lists the published versions of a template that belongs to a journey, most
        recent first. Paged by cursor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return await self._get(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/versions",
                template_id=template_id,
                notification_id=notification_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationTemplateVersionListResponse,
        )

    async def publish(
        self,
        notification_id: str,
        *,
        template_id: str,
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
        """Publishes a journey-scoped template's draft as a new version.

        Pass a version
        instead to roll back the template to an earlier publish.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
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
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/publish",
                template_id=template_id,
                notification_id=notification_id,
            ),
            body=await async_maybe_transform({"version": version}, template_publish_params.TemplatePublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def put_content(
        self,
        notification_id: str,
        *,
        template_id: str,
        content: template_put_content_params.Content,
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """
        Replace the elemental content of a journey-scoped notification template.
        Overwrites all elements in the template draft with the provided content.

        Args:
          content: Elemental content payload. The server defaults `version` when omitted.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return await self._put(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/content",
                template_id=template_id,
                notification_id=notification_id,
            ),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "state": state,
                },
                template_put_content_params.TemplatePutContentParams,
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
        template_id: str,
        notification_id: str,
        elements: Iterable[template_put_locale_params.Element],
        state: NotificationTemplateState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentMutationResponse:
        """Set locale-specific content overrides for a journey-scoped notification
        template.

        Each element override must reference an existing element by ID.

        Args:
          elements: Elements with locale-specific content overrides.

          state: Template state. Defaults to `DRAFT`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        if not locale_id:
            raise ValueError(f"Expected a non-empty value for `locale_id` but received {locale_id!r}")
        return await self._put(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/locales/{locale_id}",
                template_id=template_id,
                notification_id=notification_id,
                locale_id=locale_id,
            ),
            body=await async_maybe_transform(
                {
                    "elements": elements,
                    "state": state,
                },
                template_put_locale_params.TemplatePutLocaleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationContentMutationResponse,
        )

    async def replace(
        self,
        notification_id: str,
        *,
        template_id: str,
        notification: template_replace_params.Notification,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyTemplateGetResponse:
        """Replaces the draft content of one journey's notification template.

        Publish it
        before send nodes referencing it render the change.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return await self._put(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}",
                template_id=template_id,
                notification_id=notification_id,
            ),
            body=await async_maybe_transform(
                {
                    "notification": notification,
                    "state": state,
                },
                template_replace_params.TemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyTemplateGetResponse,
        )

    async def retrieve_content(
        self,
        notification_id: str,
        *,
        template_id: str,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationContentGetResponse:
        """
        Returns the Elemental elements and version of a journey-scoped template's
        content. Compare versions to see what changed between publishes.

        Args:
          version: Accepts `draft`, `published`, or a version string (e.g., `v001`). Defaults to
              `published`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return await self._get(
            path_template(
                "/journeys/{template_id}/templates/{notification_id}/content",
                template_id=template_id,
                notification_id=notification_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, template_retrieve_content_params.TemplateRetrieveContentParams
                ),
            ),
            cast_to=NotificationContentGetResponse,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_raw_response_wrapper(
            templates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            templates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            templates.list,
        )
        self.archive = to_raw_response_wrapper(
            templates.archive,
        )
        self.list_versions = to_raw_response_wrapper(
            templates.list_versions,
        )
        self.publish = to_raw_response_wrapper(
            templates.publish,
        )
        self.put_content = to_raw_response_wrapper(
            templates.put_content,
        )
        self.put_locale = to_raw_response_wrapper(
            templates.put_locale,
        )
        self.replace = to_raw_response_wrapper(
            templates.replace,
        )
        self.retrieve_content = to_raw_response_wrapper(
            templates.retrieve_content,
        )


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_raw_response_wrapper(
            templates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            templates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            templates.list,
        )
        self.archive = async_to_raw_response_wrapper(
            templates.archive,
        )
        self.list_versions = async_to_raw_response_wrapper(
            templates.list_versions,
        )
        self.publish = async_to_raw_response_wrapper(
            templates.publish,
        )
        self.put_content = async_to_raw_response_wrapper(
            templates.put_content,
        )
        self.put_locale = async_to_raw_response_wrapper(
            templates.put_locale,
        )
        self.replace = async_to_raw_response_wrapper(
            templates.replace,
        )
        self.retrieve_content = async_to_raw_response_wrapper(
            templates.retrieve_content,
        )


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_streamed_response_wrapper(
            templates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            templates.list,
        )
        self.archive = to_streamed_response_wrapper(
            templates.archive,
        )
        self.list_versions = to_streamed_response_wrapper(
            templates.list_versions,
        )
        self.publish = to_streamed_response_wrapper(
            templates.publish,
        )
        self.put_content = to_streamed_response_wrapper(
            templates.put_content,
        )
        self.put_locale = to_streamed_response_wrapper(
            templates.put_locale,
        )
        self.replace = to_streamed_response_wrapper(
            templates.replace,
        )
        self.retrieve_content = to_streamed_response_wrapper(
            templates.retrieve_content,
        )


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_streamed_response_wrapper(
            templates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            templates.archive,
        )
        self.list_versions = async_to_streamed_response_wrapper(
            templates.list_versions,
        )
        self.publish = async_to_streamed_response_wrapper(
            templates.publish,
        )
        self.put_content = async_to_streamed_response_wrapper(
            templates.put_content,
        )
        self.put_locale = async_to_streamed_response_wrapper(
            templates.put_locale,
        )
        self.replace = async_to_streamed_response_wrapper(
            templates.replace,
        )
        self.retrieve_content = async_to_streamed_response_wrapper(
            templates.retrieve_content,
        )
