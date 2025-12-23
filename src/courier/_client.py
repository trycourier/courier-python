# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import CourierError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        auth,
        bulk,
        send,
        lists,
        users,
        brands,
        inbound,
        tenants,
        messages,
        profiles,
        requests,
        audiences,
        automations,
        audit_events,
        translations,
        notifications,
    )
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.bulk import BulkResource, AsyncBulkResource
    from .resources.send import SendResource, AsyncSendResource
    from .resources.brands import BrandsResource, AsyncBrandsResource
    from .resources.inbound import InboundResource, AsyncInboundResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.requests import RequestsResource, AsyncRequestsResource
    from .resources.audiences import AudiencesResource, AsyncAudiencesResource
    from .resources.lists.lists import ListsResource, AsyncListsResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.audit_events import AuditEventsResource, AsyncAuditEventsResource
    from .resources.translations import TranslationsResource, AsyncTranslationsResource
    from .resources.tenants.tenants import TenantsResource, AsyncTenantsResource
    from .resources.profiles.profiles import ProfilesResource, AsyncProfilesResource
    from .resources.automations.automations import AutomationsResource, AsyncAutomationsResource
    from .resources.notifications.notifications import NotificationsResource, AsyncNotificationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Courier", "AsyncCourier", "Client", "AsyncClient"]


class Courier(SyncAPIClient):
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

    @cached_property
    def send(self) -> SendResource:
        from .resources.send import SendResource

        return SendResource(self)

    @cached_property
    def audiences(self) -> AudiencesResource:
        from .resources.audiences import AudiencesResource

        return AudiencesResource(self)

    @cached_property
    def audit_events(self) -> AuditEventsResource:
        from .resources.audit_events import AuditEventsResource

        return AuditEventsResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def automations(self) -> AutomationsResource:
        from .resources.automations import AutomationsResource

        return AutomationsResource(self)

    @cached_property
    def brands(self) -> BrandsResource:
        from .resources.brands import BrandsResource

        return BrandsResource(self)

    @cached_property
    def bulk(self) -> BulkResource:
        from .resources.bulk import BulkResource

        return BulkResource(self)

    @cached_property
    def inbound(self) -> InboundResource:
        from .resources.inbound import InboundResource

        return InboundResource(self)

    @cached_property
    def lists(self) -> ListsResource:
        from .resources.lists import ListsResource

        return ListsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def requests(self) -> RequestsResource:
        from .resources.requests import RequestsResource

        return RequestsResource(self)

    @cached_property
    def notifications(self) -> NotificationsResource:
        from .resources.notifications import NotificationsResource

        return NotificationsResource(self)

    @cached_property
    def profiles(self) -> ProfilesResource:
        from .resources.profiles import ProfilesResource

        return ProfilesResource(self)

    @cached_property
    def tenants(self) -> TenantsResource:
        from .resources.tenants import TenantsResource

        return TenantsResource(self)

    @cached_property
    def translations(self) -> TranslationsResource:
        from .resources.translations import TranslationsResource

        return TranslationsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def with_raw_response(self) -> CourierWithRawResponse:
        return CourierWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CourierWithStreamedResponse:
        return CourierWithStreamedResponse(self)

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

    @cached_property
    def send(self) -> AsyncSendResource:
        from .resources.send import AsyncSendResource

        return AsyncSendResource(self)

    @cached_property
    def audiences(self) -> AsyncAudiencesResource:
        from .resources.audiences import AsyncAudiencesResource

        return AsyncAudiencesResource(self)

    @cached_property
    def audit_events(self) -> AsyncAuditEventsResource:
        from .resources.audit_events import AsyncAuditEventsResource

        return AsyncAuditEventsResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def automations(self) -> AsyncAutomationsResource:
        from .resources.automations import AsyncAutomationsResource

        return AsyncAutomationsResource(self)

    @cached_property
    def brands(self) -> AsyncBrandsResource:
        from .resources.brands import AsyncBrandsResource

        return AsyncBrandsResource(self)

    @cached_property
    def bulk(self) -> AsyncBulkResource:
        from .resources.bulk import AsyncBulkResource

        return AsyncBulkResource(self)

    @cached_property
    def inbound(self) -> AsyncInboundResource:
        from .resources.inbound import AsyncInboundResource

        return AsyncInboundResource(self)

    @cached_property
    def lists(self) -> AsyncListsResource:
        from .resources.lists import AsyncListsResource

        return AsyncListsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def requests(self) -> AsyncRequestsResource:
        from .resources.requests import AsyncRequestsResource

        return AsyncRequestsResource(self)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        from .resources.notifications import AsyncNotificationsResource

        return AsyncNotificationsResource(self)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        from .resources.profiles import AsyncProfilesResource

        return AsyncProfilesResource(self)

    @cached_property
    def tenants(self) -> AsyncTenantsResource:
        from .resources.tenants import AsyncTenantsResource

        return AsyncTenantsResource(self)

    @cached_property
    def translations(self) -> AsyncTranslationsResource:
        from .resources.translations import AsyncTranslationsResource

        return AsyncTranslationsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCourierWithRawResponse:
        return AsyncCourierWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCourierWithStreamedResponse:
        return AsyncCourierWithStreamedResponse(self)

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
    _client: Courier

    def __init__(self, client: Courier) -> None:
        self._client = client

    @cached_property
    def send(self) -> send.SendResourceWithRawResponse:
        from .resources.send import SendResourceWithRawResponse

        return SendResourceWithRawResponse(self._client.send)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithRawResponse:
        from .resources.audiences import AudiencesResourceWithRawResponse

        return AudiencesResourceWithRawResponse(self._client.audiences)

    @cached_property
    def audit_events(self) -> audit_events.AuditEventsResourceWithRawResponse:
        from .resources.audit_events import AuditEventsResourceWithRawResponse

        return AuditEventsResourceWithRawResponse(self._client.audit_events)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def automations(self) -> automations.AutomationsResourceWithRawResponse:
        from .resources.automations import AutomationsResourceWithRawResponse

        return AutomationsResourceWithRawResponse(self._client.automations)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithRawResponse:
        from .resources.brands import BrandsResourceWithRawResponse

        return BrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def bulk(self) -> bulk.BulkResourceWithRawResponse:
        from .resources.bulk import BulkResourceWithRawResponse

        return BulkResourceWithRawResponse(self._client.bulk)

    @cached_property
    def inbound(self) -> inbound.InboundResourceWithRawResponse:
        from .resources.inbound import InboundResourceWithRawResponse

        return InboundResourceWithRawResponse(self._client.inbound)

    @cached_property
    def lists(self) -> lists.ListsResourceWithRawResponse:
        from .resources.lists import ListsResourceWithRawResponse

        return ListsResourceWithRawResponse(self._client.lists)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def requests(self) -> requests.RequestsResourceWithRawResponse:
        from .resources.requests import RequestsResourceWithRawResponse

        return RequestsResourceWithRawResponse(self._client.requests)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithRawResponse:
        from .resources.notifications import NotificationsResourceWithRawResponse

        return NotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithRawResponse:
        from .resources.profiles import ProfilesResourceWithRawResponse

        return ProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def tenants(self) -> tenants.TenantsResourceWithRawResponse:
        from .resources.tenants import TenantsResourceWithRawResponse

        return TenantsResourceWithRawResponse(self._client.tenants)

    @cached_property
    def translations(self) -> translations.TranslationsResourceWithRawResponse:
        from .resources.translations import TranslationsResourceWithRawResponse

        return TranslationsResourceWithRawResponse(self._client.translations)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)


class AsyncCourierWithRawResponse:
    _client: AsyncCourier

    def __init__(self, client: AsyncCourier) -> None:
        self._client = client

    @cached_property
    def send(self) -> send.AsyncSendResourceWithRawResponse:
        from .resources.send import AsyncSendResourceWithRawResponse

        return AsyncSendResourceWithRawResponse(self._client.send)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithRawResponse:
        from .resources.audiences import AsyncAudiencesResourceWithRawResponse

        return AsyncAudiencesResourceWithRawResponse(self._client.audiences)

    @cached_property
    def audit_events(self) -> audit_events.AsyncAuditEventsResourceWithRawResponse:
        from .resources.audit_events import AsyncAuditEventsResourceWithRawResponse

        return AsyncAuditEventsResourceWithRawResponse(self._client.audit_events)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def automations(self) -> automations.AsyncAutomationsResourceWithRawResponse:
        from .resources.automations import AsyncAutomationsResourceWithRawResponse

        return AsyncAutomationsResourceWithRawResponse(self._client.automations)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithRawResponse:
        from .resources.brands import AsyncBrandsResourceWithRawResponse

        return AsyncBrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def bulk(self) -> bulk.AsyncBulkResourceWithRawResponse:
        from .resources.bulk import AsyncBulkResourceWithRawResponse

        return AsyncBulkResourceWithRawResponse(self._client.bulk)

    @cached_property
    def inbound(self) -> inbound.AsyncInboundResourceWithRawResponse:
        from .resources.inbound import AsyncInboundResourceWithRawResponse

        return AsyncInboundResourceWithRawResponse(self._client.inbound)

    @cached_property
    def lists(self) -> lists.AsyncListsResourceWithRawResponse:
        from .resources.lists import AsyncListsResourceWithRawResponse

        return AsyncListsResourceWithRawResponse(self._client.lists)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def requests(self) -> requests.AsyncRequestsResourceWithRawResponse:
        from .resources.requests import AsyncRequestsResourceWithRawResponse

        return AsyncRequestsResourceWithRawResponse(self._client.requests)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithRawResponse:
        from .resources.notifications import AsyncNotificationsResourceWithRawResponse

        return AsyncNotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithRawResponse:
        from .resources.profiles import AsyncProfilesResourceWithRawResponse

        return AsyncProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def tenants(self) -> tenants.AsyncTenantsResourceWithRawResponse:
        from .resources.tenants import AsyncTenantsResourceWithRawResponse

        return AsyncTenantsResourceWithRawResponse(self._client.tenants)

    @cached_property
    def translations(self) -> translations.AsyncTranslationsResourceWithRawResponse:
        from .resources.translations import AsyncTranslationsResourceWithRawResponse

        return AsyncTranslationsResourceWithRawResponse(self._client.translations)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)


class CourierWithStreamedResponse:
    _client: Courier

    def __init__(self, client: Courier) -> None:
        self._client = client

    @cached_property
    def send(self) -> send.SendResourceWithStreamingResponse:
        from .resources.send import SendResourceWithStreamingResponse

        return SendResourceWithStreamingResponse(self._client.send)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithStreamingResponse:
        from .resources.audiences import AudiencesResourceWithStreamingResponse

        return AudiencesResourceWithStreamingResponse(self._client.audiences)

    @cached_property
    def audit_events(self) -> audit_events.AuditEventsResourceWithStreamingResponse:
        from .resources.audit_events import AuditEventsResourceWithStreamingResponse

        return AuditEventsResourceWithStreamingResponse(self._client.audit_events)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def automations(self) -> automations.AutomationsResourceWithStreamingResponse:
        from .resources.automations import AutomationsResourceWithStreamingResponse

        return AutomationsResourceWithStreamingResponse(self._client.automations)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithStreamingResponse:
        from .resources.brands import BrandsResourceWithStreamingResponse

        return BrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def bulk(self) -> bulk.BulkResourceWithStreamingResponse:
        from .resources.bulk import BulkResourceWithStreamingResponse

        return BulkResourceWithStreamingResponse(self._client.bulk)

    @cached_property
    def inbound(self) -> inbound.InboundResourceWithStreamingResponse:
        from .resources.inbound import InboundResourceWithStreamingResponse

        return InboundResourceWithStreamingResponse(self._client.inbound)

    @cached_property
    def lists(self) -> lists.ListsResourceWithStreamingResponse:
        from .resources.lists import ListsResourceWithStreamingResponse

        return ListsResourceWithStreamingResponse(self._client.lists)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def requests(self) -> requests.RequestsResourceWithStreamingResponse:
        from .resources.requests import RequestsResourceWithStreamingResponse

        return RequestsResourceWithStreamingResponse(self._client.requests)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithStreamingResponse:
        from .resources.notifications import NotificationsResourceWithStreamingResponse

        return NotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithStreamingResponse:
        from .resources.profiles import ProfilesResourceWithStreamingResponse

        return ProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def tenants(self) -> tenants.TenantsResourceWithStreamingResponse:
        from .resources.tenants import TenantsResourceWithStreamingResponse

        return TenantsResourceWithStreamingResponse(self._client.tenants)

    @cached_property
    def translations(self) -> translations.TranslationsResourceWithStreamingResponse:
        from .resources.translations import TranslationsResourceWithStreamingResponse

        return TranslationsResourceWithStreamingResponse(self._client.translations)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)


class AsyncCourierWithStreamedResponse:
    _client: AsyncCourier

    def __init__(self, client: AsyncCourier) -> None:
        self._client = client

    @cached_property
    def send(self) -> send.AsyncSendResourceWithStreamingResponse:
        from .resources.send import AsyncSendResourceWithStreamingResponse

        return AsyncSendResourceWithStreamingResponse(self._client.send)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithStreamingResponse:
        from .resources.audiences import AsyncAudiencesResourceWithStreamingResponse

        return AsyncAudiencesResourceWithStreamingResponse(self._client.audiences)

    @cached_property
    def audit_events(self) -> audit_events.AsyncAuditEventsResourceWithStreamingResponse:
        from .resources.audit_events import AsyncAuditEventsResourceWithStreamingResponse

        return AsyncAuditEventsResourceWithStreamingResponse(self._client.audit_events)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def automations(self) -> automations.AsyncAutomationsResourceWithStreamingResponse:
        from .resources.automations import AsyncAutomationsResourceWithStreamingResponse

        return AsyncAutomationsResourceWithStreamingResponse(self._client.automations)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithStreamingResponse:
        from .resources.brands import AsyncBrandsResourceWithStreamingResponse

        return AsyncBrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def bulk(self) -> bulk.AsyncBulkResourceWithStreamingResponse:
        from .resources.bulk import AsyncBulkResourceWithStreamingResponse

        return AsyncBulkResourceWithStreamingResponse(self._client.bulk)

    @cached_property
    def inbound(self) -> inbound.AsyncInboundResourceWithStreamingResponse:
        from .resources.inbound import AsyncInboundResourceWithStreamingResponse

        return AsyncInboundResourceWithStreamingResponse(self._client.inbound)

    @cached_property
    def lists(self) -> lists.AsyncListsResourceWithStreamingResponse:
        from .resources.lists import AsyncListsResourceWithStreamingResponse

        return AsyncListsResourceWithStreamingResponse(self._client.lists)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def requests(self) -> requests.AsyncRequestsResourceWithStreamingResponse:
        from .resources.requests import AsyncRequestsResourceWithStreamingResponse

        return AsyncRequestsResourceWithStreamingResponse(self._client.requests)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithStreamingResponse:
        from .resources.notifications import AsyncNotificationsResourceWithStreamingResponse

        return AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithStreamingResponse:
        from .resources.profiles import AsyncProfilesResourceWithStreamingResponse

        return AsyncProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def tenants(self) -> tenants.AsyncTenantsResourceWithStreamingResponse:
        from .resources.tenants import AsyncTenantsResourceWithStreamingResponse

        return AsyncTenantsResourceWithStreamingResponse(self._client.tenants)

    @cached_property
    def translations(self) -> translations.AsyncTranslationsResourceWithStreamingResponse:
        from .resources.translations import AsyncTranslationsResourceWithStreamingResponse

        return AsyncTranslationsResourceWithStreamingResponse(self._client.translations)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)


Client = Courier

AsyncClient = AsyncCourier
