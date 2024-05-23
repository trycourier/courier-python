# This file was auto-generated by Fern from our API Definition.

import os
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx

from .audiences.client import AsyncAudiencesClient, AudiencesClient
from .audit_events.client import AsyncAuditEventsClient, AuditEventsClient
from .auth_tokens.client import AsyncAuthTokensClient, AuthTokensClient
from .automations.client import AsyncAutomationsClient, AutomationsClient
from .brands.client import AsyncBrandsClient, BrandsClient
from .bulk.client import AsyncBulkClient, BulkClient
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.jsonable_encoder import jsonable_encoder
from .core.query_encoder import encode_query
from .core.remove_none_from_dict import remove_none_from_dict
from .core.request_options import RequestOptions
from .core.unchecked_base_model import construct_type
from .environment import CourierEnvironment
from .lists.client import AsyncListsClient, ListsClient
from .messages.client import AsyncMessagesClient, MessagesClient
from .notifications.client import AsyncNotificationsClient, NotificationsClient
from .profiles.client import AsyncProfilesClient, ProfilesClient
from .send.types.message import Message
from .templates.client import AsyncTemplatesClient, TemplatesClient
from .tenants.client import AsyncTenantsClient, TenantsClient
from .translations.client import AsyncTranslationsClient, TranslationsClient
from .types.send_message_response import SendMessageResponse
from .users.client import AsyncUsersClient, UsersClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class Courier:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : CourierEnvironment
        The environment to use for requests from the client. from .environment import CourierEnvironment



        Defaults to CourierEnvironment.PRODUCTION



    authorization_token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from courier.client import Courier

    client = Courier(
        authorization_token="YOUR_AUTHORIZATION_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: CourierEnvironment = CourierEnvironment.PRODUCTION,
        authorization_token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv(
            "COURIER_AUTH_TOKEN"
        ),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        if authorization_token is None:
            raise ApiError(
                body="The client must be instantiated be either passing in authorization_token or setting COURIER_AUTH_TOKEN"
            )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            authorization_token=authorization_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.audiences = AudiencesClient(client_wrapper=self._client_wrapper)
        self.audit_events = AuditEventsClient(client_wrapper=self._client_wrapper)
        self.auth_tokens = AuthTokensClient(client_wrapper=self._client_wrapper)
        self.automations = AutomationsClient(client_wrapper=self._client_wrapper)
        self.brands = BrandsClient(client_wrapper=self._client_wrapper)
        self.bulk = BulkClient(client_wrapper=self._client_wrapper)
        self.lists = ListsClient(client_wrapper=self._client_wrapper)
        self.messages = MessagesClient(client_wrapper=self._client_wrapper)
        self.notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        self.profiles = ProfilesClient(client_wrapper=self._client_wrapper)
        self.templates = TemplatesClient(client_wrapper=self._client_wrapper)
        self.tenants = TenantsClient(client_wrapper=self._client_wrapper)
        self.translations = TranslationsClient(client_wrapper=self._client_wrapper)
        self.users = UsersClient(client_wrapper=self._client_wrapper)

    def send(
        self,
        *,
        message: Message,
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendMessageResponse:
        """
        Use the send API to send a message to one or more recipients.

        Parameters
        ----------
        message : Message
            Defines the message to be delivered

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendMessageResponse

        Examples
        --------
        from courier import (
            AudienceRecipient,
            Channel,
            ContentMessage,
            Delay,
            ElementalContent,
            Expiry,
            MessageContext,
            MessageMetadata,
            MessageProvidersType,
            Routing,
            Timeout,
        )
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.send(
            message=ContentMessage(
                content=ElementalContent(),
                data={"string": {"key": "value"}},
                brand_id="string",
                channels={"string": Channel()},
                context=MessageContext(),
                metadata=MessageMetadata(),
                providers={"string": MessageProvidersType()},
                routing=Routing(),
                timeout=Timeout(),
                delay=Delay(),
                expiry=Expiry(),
                to=AudienceRecipient(),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "send"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder({"message": message})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"message": message}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                        "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(SendMessageResponse, construct_type(type_=SendMessageResponse, object_=_response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCourier:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : CourierEnvironment
        The environment to use for requests from the client. from .environment import CourierEnvironment



        Defaults to CourierEnvironment.PRODUCTION



    authorization_token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from courier.client import AsyncCourier

    client = AsyncCourier(
        authorization_token="YOUR_AUTHORIZATION_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: CourierEnvironment = CourierEnvironment.PRODUCTION,
        authorization_token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv(
            "COURIER_AUTH_TOKEN"
        ),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        if authorization_token is None:
            raise ApiError(
                body="The client must be instantiated be either passing in authorization_token or setting COURIER_AUTH_TOKEN"
            )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            authorization_token=authorization_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.audiences = AsyncAudiencesClient(client_wrapper=self._client_wrapper)
        self.audit_events = AsyncAuditEventsClient(client_wrapper=self._client_wrapper)
        self.auth_tokens = AsyncAuthTokensClient(client_wrapper=self._client_wrapper)
        self.automations = AsyncAutomationsClient(client_wrapper=self._client_wrapper)
        self.brands = AsyncBrandsClient(client_wrapper=self._client_wrapper)
        self.bulk = AsyncBulkClient(client_wrapper=self._client_wrapper)
        self.lists = AsyncListsClient(client_wrapper=self._client_wrapper)
        self.messages = AsyncMessagesClient(client_wrapper=self._client_wrapper)
        self.notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        self.profiles = AsyncProfilesClient(client_wrapper=self._client_wrapper)
        self.templates = AsyncTemplatesClient(client_wrapper=self._client_wrapper)
        self.tenants = AsyncTenantsClient(client_wrapper=self._client_wrapper)
        self.translations = AsyncTranslationsClient(client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)

    async def send(
        self,
        *,
        message: Message,
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendMessageResponse:
        """
        Use the send API to send a message to one or more recipients.

        Parameters
        ----------
        message : Message
            Defines the message to be delivered

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendMessageResponse

        Examples
        --------
        from courier import (
            AudienceRecipient,
            Channel,
            ContentMessage,
            Delay,
            ElementalContent,
            Expiry,
            MessageContext,
            MessageMetadata,
            MessageProvidersType,
            Routing,
            Timeout,
        )
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.send(
            message=ContentMessage(
                content=ElementalContent(),
                data={"string": {"key": "value"}},
                brand_id="string",
                channels={"string": Channel()},
                context=MessageContext(),
                metadata=MessageMetadata(),
                providers={"string": MessageProvidersType()},
                routing=Routing(),
                timeout=Timeout(),
                delay=Delay(),
                expiry=Expiry(),
                to=AudienceRecipient(),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "send"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder({"message": message})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"message": message}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                        "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(SendMessageResponse, construct_type(type_=SendMessageResponse, object_=_response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: CourierEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
