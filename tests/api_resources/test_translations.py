# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranslations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        translation = client.translations.retrieve(
            locale="locale",
            domain="domain",
        )
        assert_matches_type(str, translation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.translations.with_raw_response.retrieve(
            locale="locale",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert_matches_type(str, translation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.translations.with_streaming_response.retrieve(
            locale="locale",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = response.parse()
            assert_matches_type(str, translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            client.translations.with_raw_response.retrieve(
                locale="locale",
                domain="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale` but received ''"):
            client.translations.with_raw_response.retrieve(
                locale="",
                domain="domain",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Courier) -> None:
        translation = client.translations.update(
            locale="locale",
            domain="domain",
            body="body",
        )
        assert translation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Courier) -> None:
        response = client.translations.with_raw_response.update(
            locale="locale",
            domain="domain",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert translation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Courier) -> None:
        with client.translations.with_streaming_response.update(
            locale="locale",
            domain="domain",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = response.parse()
            assert translation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            client.translations.with_raw_response.update(
                locale="locale",
                domain="",
                body="body",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale` but received ''"):
            client.translations.with_raw_response.update(
                locale="",
                domain="domain",
                body="body",
            )


class TestAsyncTranslations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        translation = await async_client.translations.retrieve(
            locale="locale",
            domain="domain",
        )
        assert_matches_type(str, translation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.translations.with_raw_response.retrieve(
            locale="locale",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = await response.parse()
        assert_matches_type(str, translation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.translations.with_streaming_response.retrieve(
            locale="locale",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = await response.parse()
            assert_matches_type(str, translation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            await async_client.translations.with_raw_response.retrieve(
                locale="locale",
                domain="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale` but received ''"):
            await async_client.translations.with_raw_response.retrieve(
                locale="",
                domain="domain",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCourier) -> None:
        translation = await async_client.translations.update(
            locale="locale",
            domain="domain",
            body="body",
        )
        assert translation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCourier) -> None:
        response = await async_client.translations.with_raw_response.update(
            locale="locale",
            domain="domain",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = await response.parse()
        assert translation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCourier) -> None:
        async with async_client.translations.with_streaming_response.update(
            locale="locale",
            domain="domain",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = await response.parse()
            assert translation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            await async_client.translations.with_raw_response.update(
                locale="locale",
                domain="",
                body="body",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale` but received ''"):
            await async_client.translations.with_raw_response.update(
                locale="",
                domain="domain",
                body="body",
            )
