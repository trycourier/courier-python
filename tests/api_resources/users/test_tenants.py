# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types.users import (
    TenantListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        tenant = client.users.tenants.list(
            user_id="user_id",
        )
        assert_matches_type(TenantListResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        tenant = client.users.tenants.list(
            user_id="user_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(TenantListResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.users.tenants.with_raw_response.list(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(TenantListResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.users.tenants.with_streaming_response.list(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(TenantListResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tenants.with_raw_response.list(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_multiple(self, client: Courier) -> None:
        tenant = client.users.tenants.add_multiple(
            user_id="user_id",
            tenants=[{"tenant_id": "tenant_id"}],
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_multiple(self, client: Courier) -> None:
        response = client.users.tenants.with_raw_response.add_multiple(
            user_id="user_id",
            tenants=[{"tenant_id": "tenant_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_multiple(self, client: Courier) -> None:
        with client.users.tenants.with_streaming_response.add_multiple(
            user_id="user_id",
            tenants=[{"tenant_id": "tenant_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_multiple(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tenants.with_raw_response.add_multiple(
                user_id="",
                tenants=[{"tenant_id": "tenant_id"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_single(self, client: Courier) -> None:
        tenant = client.users.tenants.add_single(
            tenant_id="tenant_id",
            user_id="user_id",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_single_with_all_params(self, client: Courier) -> None:
        tenant = client.users.tenants.add_single(
            tenant_id="tenant_id",
            user_id="user_id",
            profile={"foo": "bar"},
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_single(self, client: Courier) -> None:
        response = client.users.tenants.with_raw_response.add_single(
            tenant_id="tenant_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_single(self, client: Courier) -> None:
        with client.users.tenants.with_streaming_response.add_single(
            tenant_id="tenant_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_single(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tenants.with_raw_response.add_single(
                tenant_id="tenant_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.users.tenants.with_raw_response.add_single(
                tenant_id="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_all(self, client: Courier) -> None:
        tenant = client.users.tenants.remove_all(
            "user_id",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_all(self, client: Courier) -> None:
        response = client.users.tenants.with_raw_response.remove_all(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_all(self, client: Courier) -> None:
        with client.users.tenants.with_streaming_response.remove_all(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove_all(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tenants.with_raw_response.remove_all(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_single(self, client: Courier) -> None:
        tenant = client.users.tenants.remove_single(
            tenant_id="tenant_id",
            user_id="user_id",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_single(self, client: Courier) -> None:
        response = client.users.tenants.with_raw_response.remove_single(
            tenant_id="tenant_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_single(self, client: Courier) -> None:
        with client.users.tenants.with_streaming_response.remove_single(
            tenant_id="tenant_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove_single(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tenants.with_raw_response.remove_single(
                tenant_id="tenant_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.users.tenants.with_raw_response.remove_single(
                tenant_id="",
                user_id="user_id",
            )


class TestAsyncTenants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        tenant = await async_client.users.tenants.list(
            user_id="user_id",
        )
        assert_matches_type(TenantListResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        tenant = await async_client.users.tenants.list(
            user_id="user_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(TenantListResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tenants.with_raw_response.list(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(TenantListResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tenants.with_streaming_response.list(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(TenantListResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tenants.with_raw_response.list(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_multiple(self, async_client: AsyncCourier) -> None:
        tenant = await async_client.users.tenants.add_multiple(
            user_id="user_id",
            tenants=[{"tenant_id": "tenant_id"}],
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_multiple(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tenants.with_raw_response.add_multiple(
            user_id="user_id",
            tenants=[{"tenant_id": "tenant_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_multiple(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tenants.with_streaming_response.add_multiple(
            user_id="user_id",
            tenants=[{"tenant_id": "tenant_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_multiple(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tenants.with_raw_response.add_multiple(
                user_id="",
                tenants=[{"tenant_id": "tenant_id"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_single(self, async_client: AsyncCourier) -> None:
        tenant = await async_client.users.tenants.add_single(
            tenant_id="tenant_id",
            user_id="user_id",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_single_with_all_params(self, async_client: AsyncCourier) -> None:
        tenant = await async_client.users.tenants.add_single(
            tenant_id="tenant_id",
            user_id="user_id",
            profile={"foo": "bar"},
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_single(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tenants.with_raw_response.add_single(
            tenant_id="tenant_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_single(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tenants.with_streaming_response.add_single(
            tenant_id="tenant_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_single(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tenants.with_raw_response.add_single(
                tenant_id="tenant_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.users.tenants.with_raw_response.add_single(
                tenant_id="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_all(self, async_client: AsyncCourier) -> None:
        tenant = await async_client.users.tenants.remove_all(
            "user_id",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_all(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tenants.with_raw_response.remove_all(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_all(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tenants.with_streaming_response.remove_all(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove_all(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tenants.with_raw_response.remove_all(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_single(self, async_client: AsyncCourier) -> None:
        tenant = await async_client.users.tenants.remove_single(
            tenant_id="tenant_id",
            user_id="user_id",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_single(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tenants.with_raw_response.remove_single(
            tenant_id="tenant_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_single(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tenants.with_streaming_response.remove_single(
            tenant_id="tenant_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove_single(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tenants.with_raw_response.remove_single(
                tenant_id="tenant_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.users.tenants.with_raw_response.remove_single(
                tenant_id="",
                user_id="user_id",
            )
