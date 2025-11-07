# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types.users import TokenListResponse, TokenRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        token = client.users.tokens.retrieve(
            token="token",
            user_id="user_id",
        )
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.users.tokens.with_raw_response.retrieve(
            token="token",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.users.tokens.with_streaming_response.retrieve(
            token="token",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenRetrieveResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tokens.with_raw_response.retrieve(
                token="token",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.users.tokens.with_raw_response.retrieve(
                token="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Courier) -> None:
        token = client.users.tokens.update(
            token="token",
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Courier) -> None:
        response = client.users.tokens.with_raw_response.update(
            token="token",
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Courier) -> None:
        with client.users.tokens.with_streaming_response.update(
            token="token",
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tokens.with_raw_response.update(
                token="token",
                user_id="",
                patch=[
                    {
                        "op": "op",
                        "path": "path",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.users.tokens.with_raw_response.update(
                token="",
                user_id="user_id",
                patch=[
                    {
                        "op": "op",
                        "path": "path",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        token = client.users.tokens.list(
            "user_id",
        )
        assert_matches_type(TokenListResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.users.tokens.with_raw_response.list(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenListResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.users.tokens.with_streaming_response.list(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenListResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tokens.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Courier) -> None:
        token = client.users.tokens.delete(
            token="token",
            user_id="user_id",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Courier) -> None:
        response = client.users.tokens.with_raw_response.delete(
            token="token",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Courier) -> None:
        with client.users.tokens.with_streaming_response.delete(
            token="token",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tokens.with_raw_response.delete(
                token="token",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.users.tokens.with_raw_response.delete(
                token="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_multiple(self, client: Courier) -> None:
        token = client.users.tokens.add_multiple(
            "user_id",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_multiple(self, client: Courier) -> None:
        response = client.users.tokens.with_raw_response.add_multiple(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_multiple(self, client: Courier) -> None:
        with client.users.tokens.with_streaming_response.add_multiple(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_multiple(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tokens.with_raw_response.add_multiple(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_single(self, client: Courier) -> None:
        token = client.users.tokens.add_single(
            path_token="token",
            user_id="user_id",
            body_token="token",
            provider_key="firebase-fcm",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_single_with_all_params(self, client: Courier) -> None:
        token = client.users.tokens.add_single(
            path_token="token",
            user_id="user_id",
            body_token="token",
            provider_key="firebase-fcm",
            device={
                "ad_id": "ad_id",
                "app_id": "app_id",
                "device_id": "device_id",
                "manufacturer": "manufacturer",
                "model": "model",
                "platform": "platform",
            },
            expiry_date="string",
            properties={},
            tracking={
                "ip": "ip",
                "lat": "lat",
                "long": "long",
                "os_version": "os_version",
            },
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_single(self, client: Courier) -> None:
        response = client.users.tokens.with_raw_response.add_single(
            path_token="token",
            user_id="user_id",
            body_token="token",
            provider_key="firebase-fcm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_single(self, client: Courier) -> None:
        with client.users.tokens.with_streaming_response.add_single(
            path_token="token",
            user_id="user_id",
            body_token="token",
            provider_key="firebase-fcm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_single(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.tokens.with_raw_response.add_single(
                path_token="token",
                user_id="",
                body_token="token",
                provider_key="firebase-fcm",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_token` but received ''"):
            client.users.tokens.with_raw_response.add_single(
                path_token="",
                user_id="user_id",
                body_token="token",
                provider_key="firebase-fcm",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        token = await async_client.users.tokens.retrieve(
            token="token",
            user_id="user_id",
        )
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tokens.with_raw_response.retrieve(
            token="token",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tokens.with_streaming_response.retrieve(
            token="token",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenRetrieveResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tokens.with_raw_response.retrieve(
                token="token",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.users.tokens.with_raw_response.retrieve(
                token="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCourier) -> None:
        token = await async_client.users.tokens.update(
            token="token",
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tokens.with_raw_response.update(
            token="token",
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tokens.with_streaming_response.update(
            token="token",
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tokens.with_raw_response.update(
                token="token",
                user_id="",
                patch=[
                    {
                        "op": "op",
                        "path": "path",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.users.tokens.with_raw_response.update(
                token="",
                user_id="user_id",
                patch=[
                    {
                        "op": "op",
                        "path": "path",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        token = await async_client.users.tokens.list(
            "user_id",
        )
        assert_matches_type(TokenListResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tokens.with_raw_response.list(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenListResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tokens.with_streaming_response.list(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenListResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tokens.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCourier) -> None:
        token = await async_client.users.tokens.delete(
            token="token",
            user_id="user_id",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tokens.with_raw_response.delete(
            token="token",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tokens.with_streaming_response.delete(
            token="token",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tokens.with_raw_response.delete(
                token="token",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.users.tokens.with_raw_response.delete(
                token="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_multiple(self, async_client: AsyncCourier) -> None:
        token = await async_client.users.tokens.add_multiple(
            "user_id",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_multiple(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tokens.with_raw_response.add_multiple(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_multiple(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tokens.with_streaming_response.add_multiple(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_multiple(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tokens.with_raw_response.add_multiple(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_single(self, async_client: AsyncCourier) -> None:
        token = await async_client.users.tokens.add_single(
            path_token="token",
            user_id="user_id",
            body_token="token",
            provider_key="firebase-fcm",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_single_with_all_params(self, async_client: AsyncCourier) -> None:
        token = await async_client.users.tokens.add_single(
            path_token="token",
            user_id="user_id",
            body_token="token",
            provider_key="firebase-fcm",
            device={
                "ad_id": "ad_id",
                "app_id": "app_id",
                "device_id": "device_id",
                "manufacturer": "manufacturer",
                "model": "model",
                "platform": "platform",
            },
            expiry_date="string",
            properties={},
            tracking={
                "ip": "ip",
                "lat": "lat",
                "long": "long",
                "os_version": "os_version",
            },
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_single(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.tokens.with_raw_response.add_single(
            path_token="token",
            user_id="user_id",
            body_token="token",
            provider_key="firebase-fcm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_single(self, async_client: AsyncCourier) -> None:
        async with async_client.users.tokens.with_streaming_response.add_single(
            path_token="token",
            user_id="user_id",
            body_token="token",
            provider_key="firebase-fcm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_single(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.tokens.with_raw_response.add_single(
                path_token="token",
                user_id="",
                body_token="token",
                provider_key="firebase-fcm",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_token` but received ''"):
            await async_client.users.tokens.with_raw_response.add_single(
                path_token="",
                user_id="user_id",
                body_token="token",
                provider_key="firebase-fcm",
            )
