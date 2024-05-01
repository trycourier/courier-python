# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..commons.errors.already_exists_error import AlreadyExistsError
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.conflict_error import ConflictError
from ..commons.errors.payment_required_error import PaymentRequiredError
from ..commons.types.already_exists import AlreadyExists
from ..commons.types.bad_request import BadRequest
from ..commons.types.conflict import Conflict
from ..commons.types.payment_required import PaymentRequired
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from .types.brand import Brand
from .types.brand_parameters import BrandParameters
from .types.brand_settings import BrandSettings
from .types.brand_snippets import BrandSnippets
from .types.brands_response import BrandsResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BrandsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        request: BrandParameters,
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Brand:
        """
        Parameters
        ----------
        request : BrandParameters

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Brand

        Examples
        --------
        from courier import BrandParameters, BrandSettings, BrandSnippets
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.brands.create(
            request=BrandParameters(
                id="string",
                name="string",
                settings=BrandSettings(),
                snippets=BrandSnippets(),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "brands"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic_v1.parse_obj_as(Brand, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 402:
            raise PaymentRequiredError(pydantic_v1.parse_obj_as(PaymentRequired, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise AlreadyExistsError(pydantic_v1.parse_obj_as(AlreadyExists, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, brand_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Brand:
        """
        Fetch a specific brand by brand ID.

        Parameters
        ----------
        brand_id : str
            A unique identifier associated with the brand you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Brand

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.brands.get(
            brand_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{jsonable_encoder(brand_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
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
            return pydantic_v1.parse_obj_as(Brand, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self, *, cursor: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> BrandsResponse:
        """
        Get the list of brands.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of brands.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrandsResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.brands.list(
            cursor="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "brands"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "cursor": cursor,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
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
            return pydantic_v1.parse_obj_as(BrandsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, brand_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a brand by brand ID.

        Parameters
        ----------
        brand_id : str
            A unique identifier associated with the brand you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.brands.delete(
            brand_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{jsonable_encoder(brand_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
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
            return
        if _response.status_code == 409:
            raise ConflictError(pydantic_v1.parse_obj_as(Conflict, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def replace(
        self,
        brand_id: str,
        *,
        name: str,
        settings: typing.Optional[BrandSettings] = OMIT,
        snippets: typing.Optional[BrandSnippets] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Brand:
        """
        Replace an existing brand with the supplied values.

        Parameters
        ----------
        brand_id : str
            A unique identifier associated with the brand you wish to update.

        name : str
            The name of the brand.

        settings : typing.Optional[BrandSettings]

        snippets : typing.Optional[BrandSnippets]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Brand

        Examples
        --------
        from courier import (
            BrandColors,
            BrandSettings,
            BrandSnippet,
            BrandSnippets,
            Email,
        )
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.brands.replace(
            brand_id="string",
            name="string",
            settings=BrandSettings(
                colors=BrandColors(),
                inapp={"key": "value"},
                email=Email(),
            ),
            snippets=BrandSnippets(
                items=[
                    BrandSnippet(
                        format="handlebars",
                        name="string",
                        value="string",
                    )
                ],
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if settings is not OMIT:
            _request["settings"] = settings
        if snippets is not OMIT:
            _request["snippets"] = snippets
        _response = self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{jsonable_encoder(brand_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
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
            return pydantic_v1.parse_obj_as(Brand, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncBrandsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        request: BrandParameters,
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Brand:
        """
        Parameters
        ----------
        request : BrandParameters

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Brand

        Examples
        --------
        from courier import BrandParameters, BrandSettings, BrandSnippets
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.brands.create(
            request=BrandParameters(
                id="string",
                name="string",
                settings=BrandSettings(),
                snippets=BrandSnippets(),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "brands"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic_v1.parse_obj_as(Brand, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 402:
            raise PaymentRequiredError(pydantic_v1.parse_obj_as(PaymentRequired, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise AlreadyExistsError(pydantic_v1.parse_obj_as(AlreadyExists, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, brand_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Brand:
        """
        Fetch a specific brand by brand ID.

        Parameters
        ----------
        brand_id : str
            A unique identifier associated with the brand you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Brand

        Examples
        --------
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.brands.get(
            brand_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{jsonable_encoder(brand_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
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
            return pydantic_v1.parse_obj_as(Brand, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self, *, cursor: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> BrandsResponse:
        """
        Get the list of brands.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of brands.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrandsResponse

        Examples
        --------
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.brands.list(
            cursor="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "brands"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "cursor": cursor,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
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
            return pydantic_v1.parse_obj_as(BrandsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, brand_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a brand by brand ID.

        Parameters
        ----------
        brand_id : str
            A unique identifier associated with the brand you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.brands.delete(
            brand_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{jsonable_encoder(brand_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
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
            return
        if _response.status_code == 409:
            raise ConflictError(pydantic_v1.parse_obj_as(Conflict, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def replace(
        self,
        brand_id: str,
        *,
        name: str,
        settings: typing.Optional[BrandSettings] = OMIT,
        snippets: typing.Optional[BrandSnippets] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Brand:
        """
        Replace an existing brand with the supplied values.

        Parameters
        ----------
        brand_id : str
            A unique identifier associated with the brand you wish to update.

        name : str
            The name of the brand.

        settings : typing.Optional[BrandSettings]

        snippets : typing.Optional[BrandSnippets]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Brand

        Examples
        --------
        from courier import (
            BrandColors,
            BrandSettings,
            BrandSnippet,
            BrandSnippets,
            Email,
        )
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.brands.replace(
            brand_id="string",
            name="string",
            settings=BrandSettings(
                colors=BrandColors(),
                inapp={"key": "value"},
                email=Email(),
            ),
            snippets=BrandSnippets(
                items=[
                    BrandSnippet(
                        format="handlebars",
                        name="string",
                        value="string",
                    )
                ],
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if settings is not OMIT:
            _request["settings"] = settings
        if snippets is not OMIT:
            _request["snippets"] = snippets
        _response = await self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{jsonable_encoder(brand_id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
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
            return pydantic_v1.parse_obj_as(Brand, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
