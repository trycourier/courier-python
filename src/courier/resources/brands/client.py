# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.errors.already_exists_error import AlreadyExistsError
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.conflict_error import ConflictError
from ..commons.errors.payment_required_error import PaymentRequiredError
from ..commons.types.already_exists import AlreadyExists
from ..commons.types.bad_request import BadRequest
from ..commons.types.conflict import Conflict
from ..commons.types.payment_required import PaymentRequired
from .types.brand import Brand
from .types.brand_parameters import BrandParameters
from .types.brand_settings import BrandSettings
from .types.brand_snippets import BrandSnippets
from .types.brands_response import BrandsResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BrandsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, request: BrandParameters) -> Brand:
        """
        Parameters:
            - request: BrandParameters.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "brands"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Brand, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 402:
            raise PaymentRequiredError(pydantic.parse_obj_as(PaymentRequired, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise AlreadyExistsError(pydantic.parse_obj_as(AlreadyExists, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, brand_id: str) -> Brand:
        """
        Fetch a specific brand by brand ID.

        Parameters:
            - brand_id: str. A unique identifier associated with the brand you wish to retrieve.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{brand_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Brand, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(self, *, cursor: typing.Optional[str] = None) -> BrandsResponse:
        """
        Get the list of brands.

        Parameters:
            - cursor: typing.Optional[str]. A unique identifier that allows for fetching the next set of brands.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "brands"),
            params=remove_none_from_dict({"cursor": cursor}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BrandsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, brand_id: str) -> None:
        """
        Delete a brand by brand ID.

        Parameters:
            - brand_id: str. A unique identifier associated with the brand you wish to retrieve.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{brand_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(Conflict, _response.json()))  # type: ignore
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
    ) -> Brand:
        """
        Replace an existing brand with the supplied values.

        Parameters:
            - brand_id: str. A unique identifier associated with the brand you wish to update.

            - name: str. The name of the brand.

            - settings: typing.Optional[BrandSettings].

            - snippets: typing.Optional[BrandSnippets].
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if settings is not OMIT:
            _request["settings"] = settings
        if snippets is not OMIT:
            _request["snippets"] = snippets
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{brand_id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Brand, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncBrandsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(self, *, request: BrandParameters) -> Brand:
        """
        Parameters:
            - request: BrandParameters.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "brands"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Brand, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 402:
            raise PaymentRequiredError(pydantic.parse_obj_as(PaymentRequired, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise AlreadyExistsError(pydantic.parse_obj_as(AlreadyExists, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, brand_id: str) -> Brand:
        """
        Fetch a specific brand by brand ID.

        Parameters:
            - brand_id: str. A unique identifier associated with the brand you wish to retrieve.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{brand_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Brand, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(self, *, cursor: typing.Optional[str] = None) -> BrandsResponse:
        """
        Get the list of brands.

        Parameters:
            - cursor: typing.Optional[str]. A unique identifier that allows for fetching the next set of brands.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "brands"),
            params=remove_none_from_dict({"cursor": cursor}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BrandsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, brand_id: str) -> None:
        """
        Delete a brand by brand ID.

        Parameters:
            - brand_id: str. A unique identifier associated with the brand you wish to retrieve.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{brand_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(Conflict, _response.json()))  # type: ignore
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
    ) -> Brand:
        """
        Replace an existing brand with the supplied values.

        Parameters:
            - brand_id: str. A unique identifier associated with the brand you wish to update.

            - name: str. The name of the brand.

            - settings: typing.Optional[BrandSettings].

            - snippets: typing.Optional[BrandSnippets].
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if settings is not OMIT:
            _request["settings"] = settings
        if snippets is not OMIT:
            _request["snippets"] = snippets
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"brands/{brand_id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Brand, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
