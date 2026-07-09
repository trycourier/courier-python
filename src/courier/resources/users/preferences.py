# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.users import (
    preference_retrieve_params,
    preference_bulk_update_params,
    preference_bulk_replace_params,
    preference_delete_topic_params,
    preference_retrieve_topic_params,
    preference_update_or_create_topic_params,
)
from ..._base_client import make_request_options
from ...types.users.preference_retrieve_response import PreferenceRetrieveResponse
from ...types.users.preference_bulk_update_response import PreferenceBulkUpdateResponse
from ...types.users.preference_bulk_replace_response import PreferenceBulkReplaceResponse
from ...types.users.preference_retrieve_topic_response import PreferenceRetrieveTopicResponse
from ...types.users.preference_update_or_create_topic_response import PreferenceUpdateOrCreateTopicResponse

__all__ = ["PreferencesResource", "AsyncPreferencesResource"]


class PreferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return PreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return PreferencesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        user_id: str,
        *,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveResponse:
        """
        Fetch all user preferences.

        Args:
          tenant_id: Query the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tenant_id": tenant_id}, preference_retrieve_params.PreferenceRetrieveParams),
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    def bulk_replace(
        self,
        user_id: str,
        *,
        topics: Iterable[preference_bulk_replace_params.Topic],
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceBulkReplaceResponse:
        """Replace a user's complete set of preference overrides in a single request.

        The
        topics in the request body become the recipient's entire set of overrides:
        listed topics are created or updated, and every existing override that is not
        included in the body is reset to its topic default. Submitting an empty `topics`
        array is a valid clear-all that resets every existing override.

        This operation is validation-atomic (all-or-nothing): structural validation
        fails fast with a single `400`, and if any topic is semantically invalid (an
        unknown topic, a `REQUIRED` topic that cannot be opted out, or a custom routing
        request that is not available on the workspace's plan) the request returns a
        single `400` aggregating every failure in `errors` and writes nothing. On
        success it returns `200` with `items` (the complete resulting override set) and
        `deleted` (the ids of the overrides that were reset to default).

        Every `topic_id` in the response — in `items`, `deleted`, and any `errors` — is
        returned in Courier's canonical topic id form, regardless of the form supplied
        in the request.

        Args:
          topics: The complete set of topic overrides for the user. Up to 50 topics may be
              provided. Any existing override not listed here is reset to its topic default;
              an empty array resets every existing override.

          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            body=maybe_transform({"topics": topics}, preference_bulk_replace_params.PreferenceBulkReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id}, preference_bulk_replace_params.PreferenceBulkReplaceParams
                ),
            ),
            cast_to=PreferenceBulkReplaceResponse,
        )

    def bulk_update(
        self,
        user_id: str,
        *,
        topics: Iterable[preference_bulk_update_params.Topic],
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceBulkUpdateResponse:
        """
        Additively create or update a user's preferences for one or more subscription
        topics in a single request. Only the topics included in the request body are
        created or updated; any existing overrides for topics not listed are left
        untouched.

        Structural validation of the request body fails fast with a single `400`. Beyond
        that, each topic is processed independently (partial-success, not
        all-or-nothing): valid topics are written and returned in `items`, while topics
        that cannot be applied are collected in `errors` with a per-topic `reason` (for
        example an unknown topic, a `REQUIRED` topic that cannot be opted out, a custom
        routing request that is not available on the workspace's plan, or a write
        failure). The request therefore returns `200` with both lists whenever the body
        is structurally valid.

        Every `topic_id` in the response — in both `items` and `errors` — is returned in
        Courier's canonical topic id form, regardless of the form supplied in the
        request.

        Args:
          topics: The topics to create or update. Between 1 and 50 topics may be provided in a
              single request.

          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            body=maybe_transform({"topics": topics}, preference_bulk_update_params.PreferenceBulkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id}, preference_bulk_update_params.PreferenceBulkUpdateParams
                ),
            ),
            cast_to=PreferenceBulkUpdateResponse,
        )

    def delete_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a user's preferences for a specific subscription topic, resetting the
        topic to its effective default. This operation is idempotent: deleting a
        preference that does not exist succeeds with no error.

        Args:
          tenant_id: Delete the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id}, preference_delete_topic_params.PreferenceDeleteTopicParams
                ),
            ),
            cast_to=NoneType,
        )

    def retrieve_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveTopicResponse:
        """
        Fetch user preferences for a specific subscription topic.

        Args:
          tenant_id: Query the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return self._get(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id}, preference_retrieve_topic_params.PreferenceRetrieveTopicParams
                ),
            ),
            cast_to=PreferenceRetrieveTopicResponse,
        )

    def update_or_create_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        topic: preference_update_or_create_topic_params.Topic,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpdateOrCreateTopicResponse:
        """
        Update or Create user preferences for a specific subscription topic.

        Args:
          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return self._put(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            body=maybe_transform(
                {"topic": topic}, preference_update_or_create_topic_params.PreferenceUpdateOrCreateTopicParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id},
                    preference_update_or_create_topic_params.PreferenceUpdateOrCreateTopicParams,
                ),
            ),
            cast_to=PreferenceUpdateOrCreateTopicResponse,
        )


class AsyncPreferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncPreferencesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        user_id: str,
        *,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveResponse:
        """
        Fetch all user preferences.

        Args:
          tenant_id: Query the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_retrieve_params.PreferenceRetrieveParams
                ),
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    async def bulk_replace(
        self,
        user_id: str,
        *,
        topics: Iterable[preference_bulk_replace_params.Topic],
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceBulkReplaceResponse:
        """Replace a user's complete set of preference overrides in a single request.

        The
        topics in the request body become the recipient's entire set of overrides:
        listed topics are created or updated, and every existing override that is not
        included in the body is reset to its topic default. Submitting an empty `topics`
        array is a valid clear-all that resets every existing override.

        This operation is validation-atomic (all-or-nothing): structural validation
        fails fast with a single `400`, and if any topic is semantically invalid (an
        unknown topic, a `REQUIRED` topic that cannot be opted out, or a custom routing
        request that is not available on the workspace's plan) the request returns a
        single `400` aggregating every failure in `errors` and writes nothing. On
        success it returns `200` with `items` (the complete resulting override set) and
        `deleted` (the ids of the overrides that were reset to default).

        Every `topic_id` in the response — in `items`, `deleted`, and any `errors` — is
        returned in Courier's canonical topic id form, regardless of the form supplied
        in the request.

        Args:
          topics: The complete set of topic overrides for the user. Up to 50 topics may be
              provided. Any existing override not listed here is reset to its topic default;
              an empty array resets every existing override.

          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            body=await async_maybe_transform(
                {"topics": topics}, preference_bulk_replace_params.PreferenceBulkReplaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_bulk_replace_params.PreferenceBulkReplaceParams
                ),
            ),
            cast_to=PreferenceBulkReplaceResponse,
        )

    async def bulk_update(
        self,
        user_id: str,
        *,
        topics: Iterable[preference_bulk_update_params.Topic],
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceBulkUpdateResponse:
        """
        Additively create or update a user's preferences for one or more subscription
        topics in a single request. Only the topics included in the request body are
        created or updated; any existing overrides for topics not listed are left
        untouched.

        Structural validation of the request body fails fast with a single `400`. Beyond
        that, each topic is processed independently (partial-success, not
        all-or-nothing): valid topics are written and returned in `items`, while topics
        that cannot be applied are collected in `errors` with a per-topic `reason` (for
        example an unknown topic, a `REQUIRED` topic that cannot be opted out, a custom
        routing request that is not available on the workspace's plan, or a write
        failure). The request therefore returns `200` with both lists whenever the body
        is structurally valid.

        Every `topic_id` in the response — in both `items` and `errors` — is returned in
        Courier's canonical topic id form, regardless of the form supplied in the
        request.

        Args:
          topics: The topics to create or update. Between 1 and 50 topics may be provided in a
              single request.

          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            body=await async_maybe_transform(
                {"topics": topics}, preference_bulk_update_params.PreferenceBulkUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_bulk_update_params.PreferenceBulkUpdateParams
                ),
            ),
            cast_to=PreferenceBulkUpdateResponse,
        )

    async def delete_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a user's preferences for a specific subscription topic, resetting the
        topic to its effective default. This operation is idempotent: deleting a
        preference that does not exist succeeds with no error.

        Args:
          tenant_id: Delete the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_delete_topic_params.PreferenceDeleteTopicParams
                ),
            ),
            cast_to=NoneType,
        )

    async def retrieve_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveTopicResponse:
        """
        Fetch user preferences for a specific subscription topic.

        Args:
          tenant_id: Query the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return await self._get(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_retrieve_topic_params.PreferenceRetrieveTopicParams
                ),
            ),
            cast_to=PreferenceRetrieveTopicResponse,
        )

    async def update_or_create_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        topic: preference_update_or_create_topic_params.Topic,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpdateOrCreateTopicResponse:
        """
        Update or Create user preferences for a specific subscription topic.

        Args:
          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return await self._put(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            body=await async_maybe_transform(
                {"topic": topic}, preference_update_or_create_topic_params.PreferenceUpdateOrCreateTopicParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id},
                    preference_update_or_create_topic_params.PreferenceUpdateOrCreateTopicParams,
                ),
            ),
            cast_to=PreferenceUpdateOrCreateTopicResponse,
        )


class PreferencesResourceWithRawResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.bulk_replace = to_raw_response_wrapper(
            preferences.bulk_replace,
        )
        self.bulk_update = to_raw_response_wrapper(
            preferences.bulk_update,
        )
        self.delete_topic = to_raw_response_wrapper(
            preferences.delete_topic,
        )
        self.retrieve_topic = to_raw_response_wrapper(
            preferences.retrieve_topic,
        )
        self.update_or_create_topic = to_raw_response_wrapper(
            preferences.update_or_create_topic,
        )


class AsyncPreferencesResourceWithRawResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.bulk_replace = async_to_raw_response_wrapper(
            preferences.bulk_replace,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            preferences.bulk_update,
        )
        self.delete_topic = async_to_raw_response_wrapper(
            preferences.delete_topic,
        )
        self.retrieve_topic = async_to_raw_response_wrapper(
            preferences.retrieve_topic,
        )
        self.update_or_create_topic = async_to_raw_response_wrapper(
            preferences.update_or_create_topic,
        )


class PreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.bulk_replace = to_streamed_response_wrapper(
            preferences.bulk_replace,
        )
        self.bulk_update = to_streamed_response_wrapper(
            preferences.bulk_update,
        )
        self.delete_topic = to_streamed_response_wrapper(
            preferences.delete_topic,
        )
        self.retrieve_topic = to_streamed_response_wrapper(
            preferences.retrieve_topic,
        )
        self.update_or_create_topic = to_streamed_response_wrapper(
            preferences.update_or_create_topic,
        )


class AsyncPreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.bulk_replace = async_to_streamed_response_wrapper(
            preferences.bulk_replace,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            preferences.bulk_update,
        )
        self.delete_topic = async_to_streamed_response_wrapper(
            preferences.delete_topic,
        )
        self.retrieve_topic = async_to_streamed_response_wrapper(
            preferences.retrieve_topic,
        )
        self.update_or_create_topic = async_to_streamed_response_wrapper(
            preferences.update_or_create_topic,
        )
