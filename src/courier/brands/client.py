# This file was auto-generated by Fern from our API Definition.

import typing
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
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
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
        from courier import (
            BrandColors,
            BrandParameters,
            BrandSettings,
            BrandSnippet,
            BrandSnippets,
            Email,
        )
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.brands.create(
            request=BrandParameters(
                id="string",
                name="string",
                settings=BrandSettings(
                    colors=BrandColors(
                        primary="string",
                        secondary="string",
                        tertiary="string",
                    ),
                    inapp={"key": "value"},
                    email=Email(
                        footer={"key": "value"},
                        header={"key": "value"},
                    ),
                ),
                snippets=BrandSnippets(
                    items=[
                        BrandSnippet(
                            name="string",
                            value="string",
                        )
                    ],
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "brands",
            method="POST",
            json=request,
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Brand, construct_type(type_=Brand, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(PaymentRequired, construct_type(type_=PaymentRequired, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 409:
                raise AlreadyExistsError(
                    typing.cast(AlreadyExists, construct_type(type_=AlreadyExists, object_=_response.json()))  # type: ignore
                )
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
            f"brands/{jsonable_encoder(brand_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Brand, construct_type(type_=Brand, object_=_response.json()))  # type: ignore
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
            "brands", method="GET", params={"cursor": cursor}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(BrandsResponse, construct_type(type_=BrandsResponse, object_=_response.json()))  # type: ignore
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
            f"brands/{jsonable_encoder(brand_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 409:
                raise ConflictError(
                    typing.cast(Conflict, construct_type(type_=Conflict, object_=_response.json()))  # type: ignore
                )
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
                colors=BrandColors(
                    primary="string",
                    secondary="string",
                    tertiary="string",
                ),
                inapp={"key": "value"},
                email=Email(
                    footer={"key": "value"},
                    header={"key": "value"},
                ),
            ),
            snippets=BrandSnippets(
                items=[
                    BrandSnippet(
                        name="string",
                        value="string",
                    )
                ],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"brands/{jsonable_encoder(brand_id)}",
            method="PUT",
            json={"name": name, "settings": settings, "snippets": snippets},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Brand, construct_type(type_=Brand, object_=_response.json()))  # type: ignore
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
        import asyncio

        from courier import (
            BrandColors,
            BrandParameters,
            BrandSettings,
            BrandSnippet,
            BrandSnippets,
            Email,
        )
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.brands.create(
                request=BrandParameters(
                    id="string",
                    name="string",
                    settings=BrandSettings(
                        colors=BrandColors(
                            primary="string",
                            secondary="string",
                            tertiary="string",
                        ),
                        inapp={"key": "value"},
                        email=Email(
                            footer={"key": "value"},
                            header={"key": "value"},
                        ),
                    ),
                    snippets=BrandSnippets(
                        items=[
                            BrandSnippet(
                                name="string",
                                value="string",
                            )
                        ],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "brands",
            method="POST",
            json=request,
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Brand, construct_type(type_=Brand, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    typing.cast(PaymentRequired, construct_type(type_=PaymentRequired, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 409:
                raise AlreadyExistsError(
                    typing.cast(AlreadyExists, construct_type(type_=AlreadyExists, object_=_response.json()))  # type: ignore
                )
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
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.brands.get(
                brand_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"brands/{jsonable_encoder(brand_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Brand, construct_type(type_=Brand, object_=_response.json()))  # type: ignore
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
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.brands.list(
                cursor="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "brands", method="GET", params={"cursor": cursor}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(BrandsResponse, construct_type(type_=BrandsResponse, object_=_response.json()))  # type: ignore
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
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.brands.delete(
                brand_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"brands/{jsonable_encoder(brand_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 409:
                raise ConflictError(
                    typing.cast(Conflict, construct_type(type_=Conflict, object_=_response.json()))  # type: ignore
                )
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
        import asyncio

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


        async def main() -> None:
            await client.brands.replace(
                brand_id="string",
                name="string",
                settings=BrandSettings(
                    colors=BrandColors(
                        primary="string",
                        secondary="string",
                        tertiary="string",
                    ),
                    inapp={"key": "value"},
                    email=Email(
                        footer={"key": "value"},
                        header={"key": "value"},
                    ),
                ),
                snippets=BrandSnippets(
                    items=[
                        BrandSnippet(
                            name="string",
                            value="string",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"brands/{jsonable_encoder(brand_id)}",
            method="PUT",
            json={"name": name, "settings": settings, "snippets": snippets},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Brand, construct_type(type_=Brand, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
