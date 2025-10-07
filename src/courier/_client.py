# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import auth, bulk, send, brands, inbound, messages, requests, audiences, audit_events, translations
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import CourierError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.lists import lists
from .resources.users import users
from .resources.tenants import tenants
from .resources.profiles import profiles
from .resources.automations import automations
from .resources.notifications import notifications

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Courier", "AsyncCourier", "Client", "AsyncClient"]


class Courier(SyncAPIClient):
    send: send.SendResource
    audiences: audiences.AudiencesResource
    audit_events: audit_events.AuditEventsResource
    auth: auth.AuthResource
    automations: automations.AutomationsResource
    brands: brands.BrandsResource
    bulk: bulk.BulkResource
    inbound: inbound.InboundResource
    lists: lists.ListsResource
    messages: messages.MessagesResource
    requests: requests.RequestsResource
    notifications: notifications.NotificationsResource
    profiles: profiles.ProfilesResource
    tenants: tenants.TenantsResource
    translations: translations.TranslationsResource
    users: users.UsersResource
    with_raw_response: CourierWithRawResponse
    with_streaming_response: CourierWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Courier client instance.

        This automatically infers the `api_key` argument from the `COURIER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COURIER_API_KEY")
        if api_key is None:
            raise CourierError(
                "The api_key client option must be set either by passing api_key to the client or by setting the COURIER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("COURIER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.courier.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.send = send.SendResource(self)
        self.audiences = audiences.AudiencesResource(self)
        self.audit_events = audit_events.AuditEventsResource(self)
        self.auth = auth.AuthResource(self)
        self.automations = automations.AutomationsResource(self)
        self.brands = brands.BrandsResource(self)
        self.bulk = bulk.BulkResource(self)
        self.inbound = inbound.InboundResource(self)
        self.lists = lists.ListsResource(self)
        self.messages = messages.MessagesResource(self)
        self.requests = requests.RequestsResource(self)
        self.notifications = notifications.NotificationsResource(self)
        self.profiles = profiles.ProfilesResource(self)
        self.tenants = tenants.TenantsResource(self)
        self.translations = translations.TranslationsResource(self)
        self.users = users.UsersResource(self)
        self.with_raw_response = CourierWithRawResponse(self)
        self.with_streaming_response = CourierWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCourier(AsyncAPIClient):
    send: send.AsyncSendResource
    audiences: audiences.AsyncAudiencesResource
    audit_events: audit_events.AsyncAuditEventsResource
    auth: auth.AsyncAuthResource
    automations: automations.AsyncAutomationsResource
    brands: brands.AsyncBrandsResource
    bulk: bulk.AsyncBulkResource
    inbound: inbound.AsyncInboundResource
    lists: lists.AsyncListsResource
    messages: messages.AsyncMessagesResource
    requests: requests.AsyncRequestsResource
    notifications: notifications.AsyncNotificationsResource
    profiles: profiles.AsyncProfilesResource
    tenants: tenants.AsyncTenantsResource
    translations: translations.AsyncTranslationsResource
    users: users.AsyncUsersResource
    with_raw_response: AsyncCourierWithRawResponse
    with_streaming_response: AsyncCourierWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCourier client instance.

        This automatically infers the `api_key` argument from the `COURIER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COURIER_API_KEY")
        if api_key is None:
            raise CourierError(
                "The api_key client option must be set either by passing api_key to the client or by setting the COURIER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("COURIER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.courier.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.send = send.AsyncSendResource(self)
        self.audiences = audiences.AsyncAudiencesResource(self)
        self.audit_events = audit_events.AsyncAuditEventsResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.automations = automations.AsyncAutomationsResource(self)
        self.brands = brands.AsyncBrandsResource(self)
        self.bulk = bulk.AsyncBulkResource(self)
        self.inbound = inbound.AsyncInboundResource(self)
        self.lists = lists.AsyncListsResource(self)
        self.messages = messages.AsyncMessagesResource(self)
        self.requests = requests.AsyncRequestsResource(self)
        self.notifications = notifications.AsyncNotificationsResource(self)
        self.profiles = profiles.AsyncProfilesResource(self)
        self.tenants = tenants.AsyncTenantsResource(self)
        self.translations = translations.AsyncTranslationsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.with_raw_response = AsyncCourierWithRawResponse(self)
        self.with_streaming_response = AsyncCourierWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CourierWithRawResponse:
    def __init__(self, client: Courier) -> None:
        self.send = send.SendResourceWithRawResponse(client.send)
        self.audiences = audiences.AudiencesResourceWithRawResponse(client.audiences)
        self.audit_events = audit_events.AuditEventsResourceWithRawResponse(client.audit_events)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.automations = automations.AutomationsResourceWithRawResponse(client.automations)
        self.brands = brands.BrandsResourceWithRawResponse(client.brands)
        self.bulk = bulk.BulkResourceWithRawResponse(client.bulk)
        self.inbound = inbound.InboundResourceWithRawResponse(client.inbound)
        self.lists = lists.ListsResourceWithRawResponse(client.lists)
        self.messages = messages.MessagesResourceWithRawResponse(client.messages)
        self.requests = requests.RequestsResourceWithRawResponse(client.requests)
        self.notifications = notifications.NotificationsResourceWithRawResponse(client.notifications)
        self.profiles = profiles.ProfilesResourceWithRawResponse(client.profiles)
        self.tenants = tenants.TenantsResourceWithRawResponse(client.tenants)
        self.translations = translations.TranslationsResourceWithRawResponse(client.translations)
        self.users = users.UsersResourceWithRawResponse(client.users)


class AsyncCourierWithRawResponse:
    def __init__(self, client: AsyncCourier) -> None:
        self.send = send.AsyncSendResourceWithRawResponse(client.send)
        self.audiences = audiences.AsyncAudiencesResourceWithRawResponse(client.audiences)
        self.audit_events = audit_events.AsyncAuditEventsResourceWithRawResponse(client.audit_events)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.automations = automations.AsyncAutomationsResourceWithRawResponse(client.automations)
        self.brands = brands.AsyncBrandsResourceWithRawResponse(client.brands)
        self.bulk = bulk.AsyncBulkResourceWithRawResponse(client.bulk)
        self.inbound = inbound.AsyncInboundResourceWithRawResponse(client.inbound)
        self.lists = lists.AsyncListsResourceWithRawResponse(client.lists)
        self.messages = messages.AsyncMessagesResourceWithRawResponse(client.messages)
        self.requests = requests.AsyncRequestsResourceWithRawResponse(client.requests)
        self.notifications = notifications.AsyncNotificationsResourceWithRawResponse(client.notifications)
        self.profiles = profiles.AsyncProfilesResourceWithRawResponse(client.profiles)
        self.tenants = tenants.AsyncTenantsResourceWithRawResponse(client.tenants)
        self.translations = translations.AsyncTranslationsResourceWithRawResponse(client.translations)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)


class CourierWithStreamedResponse:
    def __init__(self, client: Courier) -> None:
        self.send = send.SendResourceWithStreamingResponse(client.send)
        self.audiences = audiences.AudiencesResourceWithStreamingResponse(client.audiences)
        self.audit_events = audit_events.AuditEventsResourceWithStreamingResponse(client.audit_events)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.automations = automations.AutomationsResourceWithStreamingResponse(client.automations)
        self.brands = brands.BrandsResourceWithStreamingResponse(client.brands)
        self.bulk = bulk.BulkResourceWithStreamingResponse(client.bulk)
        self.inbound = inbound.InboundResourceWithStreamingResponse(client.inbound)
        self.lists = lists.ListsResourceWithStreamingResponse(client.lists)
        self.messages = messages.MessagesResourceWithStreamingResponse(client.messages)
        self.requests = requests.RequestsResourceWithStreamingResponse(client.requests)
        self.notifications = notifications.NotificationsResourceWithStreamingResponse(client.notifications)
        self.profiles = profiles.ProfilesResourceWithStreamingResponse(client.profiles)
        self.tenants = tenants.TenantsResourceWithStreamingResponse(client.tenants)
        self.translations = translations.TranslationsResourceWithStreamingResponse(client.translations)
        self.users = users.UsersResourceWithStreamingResponse(client.users)


class AsyncCourierWithStreamedResponse:
    def __init__(self, client: AsyncCourier) -> None:
        self.send = send.AsyncSendResourceWithStreamingResponse(client.send)
        self.audiences = audiences.AsyncAudiencesResourceWithStreamingResponse(client.audiences)
        self.audit_events = audit_events.AsyncAuditEventsResourceWithStreamingResponse(client.audit_events)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.automations = automations.AsyncAutomationsResourceWithStreamingResponse(client.automations)
        self.brands = brands.AsyncBrandsResourceWithStreamingResponse(client.brands)
        self.bulk = bulk.AsyncBulkResourceWithStreamingResponse(client.bulk)
        self.inbound = inbound.AsyncInboundResourceWithStreamingResponse(client.inbound)
        self.lists = lists.AsyncListsResourceWithStreamingResponse(client.lists)
        self.messages = messages.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.requests = requests.AsyncRequestsResourceWithStreamingResponse(client.requests)
        self.notifications = notifications.AsyncNotificationsResourceWithStreamingResponse(client.notifications)
        self.profiles = profiles.AsyncProfilesResourceWithStreamingResponse(client.profiles)
        self.tenants = tenants.AsyncTenantsResourceWithStreamingResponse(client.tenants)
        self.translations = translations.AsyncTranslationsResourceWithStreamingResponse(client.translations)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)


Client = Courier

AsyncClient = AsyncCourier
