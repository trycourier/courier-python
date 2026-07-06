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
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
    @cached_property
    def templates(self) -> TemplatesResource:
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """Create a journey.

        Defaults to `DRAFT` state; pass `state: "PUBLISHED"` to
        publish on create. Send nodes are not allowed on `POST`. The standard flow is:
        create the journey shell here, add notification templates with
        `POST /journeys/{templateId}/templates`, then wire them into the journey with
        `PUT /journeys/{templateId}`. Call `POST /journeys/{templateId}/publish` to
        publish a draft after the fact.

        Args:
          state: Lifecycle state of a journey.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        """Archive a journey.

        Archived journeys cannot be invoked. Existing journey runs
        continue to completion.

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        """Cancel journey runs.

        The request body must include EXACTLY ONE of
        `cancelation_token` (cancels every run associated with the token) or `run_id`
        (cancels a single tenant-scoped run). Supplying both or neither is a `400`. A
        `run_id` that does not match a run for the tenant returns `404`. Cancelation is
        idempotent: a run that has already finished (`PROCESSED`/`ERROR`) or was already
        `CANCELED` is left unchanged and its current status is returned.

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        """Cancel journey runs.

        The request body must include EXACTLY ONE of
        `cancelation_token` (cancels every run associated with the token) or `run_id`
        (cancels a single tenant-scoped run). Supplying both or neither is a `400`. A
        `run_id` that does not match a run for the tenant returns `404`. Cancelation is
        idempotent: a run that has already finished (`PROCESSED`/`ERROR`) or was already
        `CANCELED` is left unchanged and its current status is returned.

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
        run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneysInvokeResponse:
        """Invoke a journey by id or alias to start a new run.

        The response includes a
        `runId` identifying the run.

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
        List published versions of a journey, ordered most recent first.

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """Publish the current draft as a new version.

        Body is optional; pass
        `{ "version": "vN" }` to roll back to a prior version instead. Returns 404 if
        the journey has no draft to publish.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
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
        """Replace the journey draft.

        Updates the working draft only; call
        `POST /journeys/{templateId}/publish` to make it live, or pass
        `state: "PUBLISHED"` in this request to publish immediately. Send-node
        `template` ids must already exist and be scoped to this journey, and node ids
        must not be claimed by another journey.

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
    @cached_property
    def templates(self) -> AsyncTemplatesResource:
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """Create a journey.

        Defaults to `DRAFT` state; pass `state: "PUBLISHED"` to
        publish on create. Send nodes are not allowed on `POST`. The standard flow is:
        create the journey shell here, add notification templates with
        `POST /journeys/{templateId}/templates`, then wire them into the journey with
        `PUT /journeys/{templateId}`. Call `POST /journeys/{templateId}/publish` to
        publish a draft after the fact.

        Args:
          state: Lifecycle state of a journey.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        """Archive a journey.

        Archived journeys cannot be invoked. Existing journey runs
        continue to completion.

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        """Cancel journey runs.

        The request body must include EXACTLY ONE of
        `cancelation_token` (cancels every run associated with the token) or `run_id`
        (cancels a single tenant-scoped run). Supplying both or neither is a `400`. A
        `run_id` that does not match a run for the tenant returns `404`. Cancelation is
        idempotent: a run that has already finished (`PROCESSED`/`ERROR`) or was already
        `CANCELED` is left unchanged and its current status is returned.

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
        """Cancel journey runs.

        The request body must include EXACTLY ONE of
        `cancelation_token` (cancels every run associated with the token) or `run_id`
        (cancels a single tenant-scoped run). Supplying both or neither is a `400`. A
        `run_id` that does not match a run for the tenant returns `404`. Cancelation is
        idempotent: a run that has already finished (`PROCESSED`/`ERROR`) or was already
        `CANCELED` is left unchanged and its current status is returned.

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
        run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CancelJourneyResponse:
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneysInvokeResponse:
        """Invoke a journey by id or alias to start a new run.

        The response includes a
        `runId` identifying the run.

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
        List published versions of a journey, ordered most recent first.

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JourneyResponse:
        """Publish the current draft as a new version.

        Body is optional; pass
        `{ "version": "vN" }` to roll back to a prior version instead. Returns 404 if
        the journey has no draft to publish.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
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
        """Replace the journey draft.

        Updates the working draft only; call
        `POST /journeys/{templateId}/publish` to make it live, or pass
        `state: "PUBLISHED"` in this request to publish immediately. Send-node
        `template` ids must already exist and be scoped to this journey, and node ids
        must not be claimed by another journey.

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
        return AsyncTemplatesResourceWithStreamingResponse(self._journeys.templates)
