# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    ProfileCreateResponse,
    ProfileReplaceResponse,
    ProfileRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        profile = client.profiles.create(
            user_id="user_id",
            profile={"foo": "bar"},
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.profiles.with_raw_response.create(
            user_id="user_id",
            profile={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.profiles.with_streaming_response.create(
            user_id="user_id",
            profile={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.profiles.with_raw_response.create(
                user_id="",
                profile={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        profile = client.profiles.retrieve(
            "user_id",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.profiles.with_raw_response.retrieve(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.profiles.with_streaming_response.retrieve(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Courier) -> None:
        profile = client.profiles.update(
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                    "value": "value",
                }
            ],
        )
        assert profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Courier) -> None:
        response = client.profiles.with_raw_response.update(
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Courier) -> None:
        with client.profiles.with_streaming_response.update(
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.profiles.with_raw_response.update(
                user_id="",
                patch=[
                    {
                        "op": "op",
                        "path": "path",
                        "value": "value",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Courier) -> None:
        profile = client.profiles.delete(
            "user_id",
        )
        assert profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Courier) -> None:
        response = client.profiles.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Courier) -> None:
        with client.profiles.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace(self, client: Courier) -> None:
        profile = client.profiles.replace(
            user_id="user_id",
            profile={"foo": "bar"},
        )
        assert_matches_type(ProfileReplaceResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Courier) -> None:
        response = client.profiles.with_raw_response.replace(
            user_id="user_id",
            profile={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileReplaceResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Courier) -> None:
        with client.profiles.with_streaming_response.replace(
            user_id="user_id",
            profile={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileReplaceResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.profiles.with_raw_response.replace(
                user_id="",
                profile={"foo": "bar"},
            )


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        profile = await async_client.profiles.create(
            user_id="user_id",
            profile={"foo": "bar"},
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.profiles.with_raw_response.create(
            user_id="user_id",
            profile={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.profiles.with_streaming_response.create(
            user_id="user_id",
            profile={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.profiles.with_raw_response.create(
                user_id="",
                profile={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        profile = await async_client.profiles.retrieve(
            "user_id",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.profiles.with_raw_response.retrieve(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.profiles.with_streaming_response.retrieve(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCourier) -> None:
        profile = await async_client.profiles.update(
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                    "value": "value",
                }
            ],
        )
        assert profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCourier) -> None:
        response = await async_client.profiles.with_raw_response.update(
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCourier) -> None:
        async with async_client.profiles.with_streaming_response.update(
            user_id="user_id",
            patch=[
                {
                    "op": "op",
                    "path": "path",
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.profiles.with_raw_response.update(
                user_id="",
                patch=[
                    {
                        "op": "op",
                        "path": "path",
                        "value": "value",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCourier) -> None:
        profile = await async_client.profiles.delete(
            "user_id",
        )
        assert profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCourier) -> None:
        response = await async_client.profiles.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCourier) -> None:
        async with async_client.profiles.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncCourier) -> None:
        profile = await async_client.profiles.replace(
            user_id="user_id",
            profile={"foo": "bar"},
        )
        assert_matches_type(ProfileReplaceResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCourier) -> None:
        response = await async_client.profiles.with_raw_response.replace(
            user_id="user_id",
            profile={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileReplaceResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCourier) -> None:
        async with async_client.profiles.with_streaming_response.replace(
            user_id="user_id",
            profile={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileReplaceResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.profiles.with_raw_response.replace(
                user_id="",
                profile={"foo": "bar"},
            )
