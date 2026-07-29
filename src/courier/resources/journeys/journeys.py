# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Iterable, cast
from typing_extensions import Literal, overload

import httpx

from ...types import (
    JourneyState,
    journey_list_params,
    journey_cancel_params,
    journey_create_params,
    journey_invoke_params,
    journey_publish_params,
    journey_replace_params,
    journey_retrieve_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.journey_state import JourneyState
from ...types.journey_response import JourneyResponse
from ...types.journey_node_param import JourneyNodeParam
from ...types.journeys_list_response import JourneysListResponse
from ...types.cancel_journey_response import CancelJourneyResponse
from ...types.journeys_invoke_response import JourneysInvokeResponse
from ...types.journey_versions_list_response import JourneyVersionsListResponse

__all__ = ["JourneysResource", "AsyncJourneysResource"]


class JourneysResource(SyncAPIResource):
    """
    Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
    """

    @cached_property
    def templates(self) -> TemplatesResource:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        return TemplatesResource(self._client)

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

    def create(
        self,
        *,
        name: str,
        nodes: Iterable[JourneyNodeParam],
        enabled: bool | Omit = omit,
        state: JourneyState | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """
        Creates a journey from a set of nodes, in draft state unless you pass a
        published state. Send nodes cannot be included until their templates exist.

        Args:
          state: Lifecycle state of a journey.

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
            "/journeys",
            body=maybe_transform(
                {
                    "name": name,
                    "nodes": nodes,
                    "enabled": enabled,
                    "state": state,
                },
                journey_create_params.JourneyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyResponse,
        )

    def retrieve(
        self,
        template_id: str,
        *,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """Fetch a journey by id.

        Pass `?version=draft` (default `published`) to retrieve
        the working draft, or `?version=vN` to retrieve a historical version.

        Args:
          version: Version selector: `draft`, `published` (default), or `vN`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._get(
            path_template("/journeys/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, journey_retrieve_params.JourneyRetrieveParams),
            ),
            cast_to=JourneyResponse,
        )

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
        """
        Lists the workspace's journeys, each carrying a name, state, and enabled flag.
        Paged by cursor.

        Args:
          cursor: A cursor token for pagination. Use the cursor from the previous response to
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

    def archive(
        self,
        template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archives a journey so it can no longer be invoked.

        Runs already in flight
        continue to completion, so archiving never strands a user mid-sequence.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/journeys/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    def cancel(
        self,
        *,
        cancelation_token: str,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        """
        Cancels in-flight journey runs, either every run sharing a cancelation token or
        one run by id. Use it to stop a sequence when the event resolves.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def cancel(
        self,
        *,
        run_id: str,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        """
        Cancels in-flight journey runs, either every run sharing a cancelation token or
        one run by id. Use it to stop a sequence when the event resolves.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["cancelation_token"], ["run_id"])
    def cancel(
        self,
        *,
        cancelation_token: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-idempotency-expiration": x_idempotency_expiration,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            CancelJourneyResponse,
            self._post(
                "/journeys/cancel",
                body=maybe_transform(
                    {
                        "cancelation_token": cancelation_token,
                        "run_id": run_id,
                    },
                    journey_cancel_params.JourneyCancelParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, CancelJourneyResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def invoke(
        self,
        template_id: str,
        *,
        data: Dict[str, object] | Omit = omit,
        profile: Dict[str, object] | Omit = omit,
        user_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneysInvokeResponse:
        """Starts a journey run for one user and returns a runId.

        Runs execute
        asynchronously, so the response arrives before any message is sent.

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
            path_template("/journeys/{template_id}/invoke", template_id=template_id),
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

    def list_versions(
        self,
        template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyVersionsListResponse:
        """
        Lists a journey's published versions, most recent first, so you have a version
        id to roll back to. Paged by cursor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._get(
            path_template("/journeys/{template_id}/versions", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyVersionsListResponse,
        )

    def publish(
        self,
        template_id: str,
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
    ) -> JourneyResponse:
        """
        Publishes a journey's current draft as a new version, making it live for new
        runs. Pass a version instead to roll back to an earlier one.

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
            path_template("/journeys/{template_id}/publish", template_id=template_id),
            body=maybe_transform({"version": version}, journey_publish_params.JourneyPublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyResponse,
        )

    def replace(
        self,
        template_id: str,
        *,
        name: str,
        nodes: Iterable[JourneyNodeParam],
        enabled: bool | Omit = omit,
        state: JourneyState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """
        Replaces a journey's working draft, leaving the published version live until you
        publish. Reach for this when editing a journey already running.

        Args:
          state: Lifecycle state of a journey.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._put(
            path_template("/journeys/{template_id}", template_id=template_id),
            body=maybe_transform(
                {
                    "name": name,
                    "nodes": nodes,
                    "enabled": enabled,
                    "state": state,
                },
                journey_replace_params.JourneyReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyResponse,
        )


class AsyncJourneysResource(AsyncAPIResource):
    """
    Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
    """

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        return AsyncTemplatesResource(self._client)

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

    async def create(
        self,
        *,
        name: str,
        nodes: Iterable[JourneyNodeParam],
        enabled: bool | Omit = omit,
        state: JourneyState | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """
        Creates a journey from a set of nodes, in draft state unless you pass a
        published state. Send nodes cannot be included until their templates exist.

        Args:
          state: Lifecycle state of a journey.

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
            "/journeys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "nodes": nodes,
                    "enabled": enabled,
                    "state": state,
                },
                journey_create_params.JourneyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyResponse,
        )

    async def retrieve(
        self,
        template_id: str,
        *,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """Fetch a journey by id.

        Pass `?version=draft` (default `published`) to retrieve
        the working draft, or `?version=vN` to retrieve a historical version.

        Args:
          version: Version selector: `draft`, `published` (default), or `vN`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._get(
            path_template("/journeys/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"version": version}, journey_retrieve_params.JourneyRetrieveParams),
            ),
            cast_to=JourneyResponse,
        )

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
        """
        Lists the workspace's journeys, each carrying a name, state, and enabled flag.
        Paged by cursor.

        Args:
          cursor: A cursor token for pagination. Use the cursor from the previous response to
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

    async def archive(
        self,
        template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archives a journey so it can no longer be invoked.

        Runs already in flight
        continue to completion, so archiving never strands a user mid-sequence.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/journeys/{template_id}", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    async def cancel(
        self,
        *,
        cancelation_token: str,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        """
        Cancels in-flight journey runs, either every run sharing a cancelation token or
        one run by id. Use it to stop a sequence when the event resolves.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def cancel(
        self,
        *,
        run_id: str,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        """
        Cancels in-flight journey runs, either every run sharing a cancelation token or
        one run by id. Use it to stop a sequence when the event resolves.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["cancelation_token"], ["run_id"])
    async def cancel(
        self,
        *,
        cancelation_token: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-idempotency-expiration": x_idempotency_expiration,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            CancelJourneyResponse,
            await self._post(
                "/journeys/cancel",
                body=await async_maybe_transform(
                    {
                        "cancelation_token": cancelation_token,
                        "run_id": run_id,
                    },
                    journey_cancel_params.JourneyCancelParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, CancelJourneyResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def invoke(
        self,
        template_id: str,
        *,
        data: Dict[str, object] | Omit = omit,
        profile: Dict[str, object] | Omit = omit,
        user_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneysInvokeResponse:
        """Starts a journey run for one user and returns a runId.

        Runs execute
        asynchronously, so the response arrives before any message is sent.

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
            path_template("/journeys/{template_id}/invoke", template_id=template_id),
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

    async def list_versions(
        self,
        template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyVersionsListResponse:
        """
        Lists a journey's published versions, most recent first, so you have a version
        id to roll back to. Paged by cursor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._get(
            path_template("/journeys/{template_id}/versions", template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyVersionsListResponse,
        )

    async def publish(
        self,
        template_id: str,
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
    ) -> JourneyResponse:
        """
        Publishes a journey's current draft as a new version, making it live for new
        runs. Pass a version instead to roll back to an earlier one.

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
            path_template("/journeys/{template_id}/publish", template_id=template_id),
            body=await async_maybe_transform({"version": version}, journey_publish_params.JourneyPublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyResponse,
        )

    async def replace(
        self,
        template_id: str,
        *,
        name: str,
        nodes: Iterable[JourneyNodeParam],
        enabled: bool | Omit = omit,
        state: JourneyState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """
        Replaces a journey's working draft, leaving the published version live until you
        publish. Reach for this when editing a journey already running.

        Args:
          state: Lifecycle state of a journey.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._put(
            path_template("/journeys/{template_id}", template_id=template_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "nodes": nodes,
                    "enabled": enabled,
                    "state": state,
                },
                journey_replace_params.JourneyReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JourneyResponse,
        )


class JourneysResourceWithRawResponse:
    def __init__(self, journeys: JourneysResource) -> None:
        self._journeys = journeys

        self.create = to_raw_response_wrapper(
            journeys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            journeys.retrieve,
        )
        self.list = to_raw_response_wrapper(
            journeys.list,
        )
        self.archive = to_raw_response_wrapper(
            journeys.archive,
        )
        self.cancel = to_raw_response_wrapper(
            journeys.cancel,
        )
        self.invoke = to_raw_response_wrapper(
            journeys.invoke,
        )
        self.list_versions = to_raw_response_wrapper(
            journeys.list_versions,
        )
        self.publish = to_raw_response_wrapper(
            journeys.publish,
        )
        self.replace = to_raw_response_wrapper(
            journeys.replace,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        return TemplatesResourceWithRawResponse(self._journeys.templates)


class AsyncJourneysResourceWithRawResponse:
    def __init__(self, journeys: AsyncJourneysResource) -> None:
        self._journeys = journeys

        self.create = async_to_raw_response_wrapper(
            journeys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            journeys.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            journeys.list,
        )
        self.archive = async_to_raw_response_wrapper(
            journeys.archive,
        )
        self.cancel = async_to_raw_response_wrapper(
            journeys.cancel,
        )
        self.invoke = async_to_raw_response_wrapper(
            journeys.invoke,
        )
        self.list_versions = async_to_raw_response_wrapper(
            journeys.list_versions,
        )
        self.publish = async_to_raw_response_wrapper(
            journeys.publish,
        )
        self.replace = async_to_raw_response_wrapper(
            journeys.replace,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        return AsyncTemplatesResourceWithRawResponse(self._journeys.templates)


class JourneysResourceWithStreamingResponse:
    def __init__(self, journeys: JourneysResource) -> None:
        self._journeys = journeys

        self.create = to_streamed_response_wrapper(
            journeys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            journeys.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            journeys.list,
        )
        self.archive = to_streamed_response_wrapper(
            journeys.archive,
        )
        self.cancel = to_streamed_response_wrapper(
            journeys.cancel,
        )
        self.invoke = to_streamed_response_wrapper(
            journeys.invoke,
        )
        self.list_versions = to_streamed_response_wrapper(
            journeys.list_versions,
        )
        self.publish = to_streamed_response_wrapper(
            journeys.publish,
        )
        self.replace = to_streamed_response_wrapper(
            journeys.replace,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        return TemplatesResourceWithStreamingResponse(self._journeys.templates)


class AsyncJourneysResourceWithStreamingResponse:
    def __init__(self, journeys: AsyncJourneysResource) -> None:
        self._journeys = journeys

        self.create = async_to_streamed_response_wrapper(
            journeys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            journeys.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            journeys.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            journeys.archive,
        )
        self.cancel = async_to_streamed_response_wrapper(
            journeys.cancel,
        )
        self.invoke = async_to_streamed_response_wrapper(
            journeys.invoke,
        )
        self.list_versions = async_to_streamed_response_wrapper(
            journeys.list_versions,
        )
        self.publish = async_to_streamed_response_wrapper(
            journeys.publish,
        )
        self.replace = async_to_streamed_response_wrapper(
            journeys.replace,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        return AsyncTemplatesResourceWithStreamingResponse(self._journeys.templates)
