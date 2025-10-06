# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    BulkCreateJobResponse,
    BulkListUsersResponse,
    BulkRetrieveJobResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_users(self, client: Courier) -> None:
        bulk = client.bulk.add_users(
            job_id="job_id",
            users=[{}],
        )
        assert bulk is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_users(self, client: Courier) -> None:
        response = client.bulk.with_raw_response.add_users(
            job_id="job_id",
            users=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert bulk is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_users(self, client: Courier) -> None:
        with client.bulk.with_streaming_response.add_users(
            job_id="job_id",
            users=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_users(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.bulk.with_raw_response.add_users(
                job_id="",
                users=[{}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_job(self, client: Courier) -> None:
        bulk = client.bulk.create_job(
            message={"template": "template"},
        )
        assert_matches_type(BulkCreateJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_job_with_all_params(self, client: Courier) -> None:
        bulk = client.bulk.create_job(
            message={
                "template": "template",
                "brand": "brand",
                "data": {"foo": "bar"},
                "event": "event",
                "locale": {"foo": {"foo": "bar"}},
                "override": {"foo": "bar"},
            },
        )
        assert_matches_type(BulkCreateJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_job(self, client: Courier) -> None:
        response = client.bulk.with_raw_response.create_job(
            message={"template": "template"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkCreateJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_job(self, client: Courier) -> None:
        with client.bulk.with_streaming_response.create_job(
            message={"template": "template"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkCreateJobResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_users(self, client: Courier) -> None:
        bulk = client.bulk.list_users(
            job_id="job_id",
        )
        assert_matches_type(BulkListUsersResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_users_with_all_params(self, client: Courier) -> None:
        bulk = client.bulk.list_users(
            job_id="job_id",
            cursor="cursor",
        )
        assert_matches_type(BulkListUsersResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_users(self, client: Courier) -> None:
        response = client.bulk.with_raw_response.list_users(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkListUsersResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_users(self, client: Courier) -> None:
        with client.bulk.with_streaming_response.list_users(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkListUsersResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_users(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.bulk.with_raw_response.list_users(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_job(self, client: Courier) -> None:
        bulk = client.bulk.retrieve_job(
            "job_id",
        )
        assert_matches_type(BulkRetrieveJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_job(self, client: Courier) -> None:
        response = client.bulk.with_raw_response.retrieve_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkRetrieveJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_job(self, client: Courier) -> None:
        with client.bulk.with_streaming_response.retrieve_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkRetrieveJobResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_job(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.bulk.with_raw_response.retrieve_job(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job(self, client: Courier) -> None:
        bulk = client.bulk.run_job(
            "job_id",
        )
        assert bulk is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_job(self, client: Courier) -> None:
        response = client.bulk.with_raw_response.run_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert bulk is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_job(self, client: Courier) -> None:
        with client.bulk.with_streaming_response.run_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_run_job(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.bulk.with_raw_response.run_job(
                "",
            )


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_users(self, async_client: AsyncCourier) -> None:
        bulk = await async_client.bulk.add_users(
            job_id="job_id",
            users=[{}],
        )
        assert bulk is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_users(self, async_client: AsyncCourier) -> None:
        response = await async_client.bulk.with_raw_response.add_users(
            job_id="job_id",
            users=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert bulk is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_users(self, async_client: AsyncCourier) -> None:
        async with async_client.bulk.with_streaming_response.add_users(
            job_id="job_id",
            users=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_users(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.bulk.with_raw_response.add_users(
                job_id="",
                users=[{}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_job(self, async_client: AsyncCourier) -> None:
        bulk = await async_client.bulk.create_job(
            message={"template": "template"},
        )
        assert_matches_type(BulkCreateJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_job_with_all_params(self, async_client: AsyncCourier) -> None:
        bulk = await async_client.bulk.create_job(
            message={
                "template": "template",
                "brand": "brand",
                "data": {"foo": "bar"},
                "event": "event",
                "locale": {"foo": {"foo": "bar"}},
                "override": {"foo": "bar"},
            },
        )
        assert_matches_type(BulkCreateJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_job(self, async_client: AsyncCourier) -> None:
        response = await async_client.bulk.with_raw_response.create_job(
            message={"template": "template"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkCreateJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_job(self, async_client: AsyncCourier) -> None:
        async with async_client.bulk.with_streaming_response.create_job(
            message={"template": "template"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkCreateJobResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_users(self, async_client: AsyncCourier) -> None:
        bulk = await async_client.bulk.list_users(
            job_id="job_id",
        )
        assert_matches_type(BulkListUsersResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_users_with_all_params(self, async_client: AsyncCourier) -> None:
        bulk = await async_client.bulk.list_users(
            job_id="job_id",
            cursor="cursor",
        )
        assert_matches_type(BulkListUsersResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_users(self, async_client: AsyncCourier) -> None:
        response = await async_client.bulk.with_raw_response.list_users(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkListUsersResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_users(self, async_client: AsyncCourier) -> None:
        async with async_client.bulk.with_streaming_response.list_users(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkListUsersResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_users(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.bulk.with_raw_response.list_users(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_job(self, async_client: AsyncCourier) -> None:
        bulk = await async_client.bulk.retrieve_job(
            "job_id",
        )
        assert_matches_type(BulkRetrieveJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_job(self, async_client: AsyncCourier) -> None:
        response = await async_client.bulk.with_raw_response.retrieve_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkRetrieveJobResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_job(self, async_client: AsyncCourier) -> None:
        async with async_client.bulk.with_streaming_response.retrieve_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkRetrieveJobResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_job(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.bulk.with_raw_response.retrieve_job(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job(self, async_client: AsyncCourier) -> None:
        bulk = await async_client.bulk.run_job(
            "job_id",
        )
        assert bulk is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_job(self, async_client: AsyncCourier) -> None:
        response = await async_client.bulk.with_raw_response.run_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert bulk is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_job(self, async_client: AsyncCourier) -> None:
        async with async_client.bulk.with_streaming_response.run_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_run_job(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.bulk.with_raw_response.run_job(
                "",
            )
