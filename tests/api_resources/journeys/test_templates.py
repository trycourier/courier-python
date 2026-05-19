# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    JourneyTemplateGetResponse,
    JourneyTemplateListResponse,
    NotificationTemplateVersionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        template = client.journeys.templates.create(
            template_id="x",
            channel="email",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome email",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Courier) -> None:
        template = client.journeys.templates.create(
            template_id="x",
            channel="email",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [
                        {
                            "channels": ["string"],
                            "if": "if",
                            "loop": "loop",
                            "ref": "ref",
                            "type": "text",
                        }
                    ],
                    "version": "2022-01-01",
                    "scope": "default",
                },
                "name": "Welcome email",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
            provider_key="x",
            state="state",
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.journeys.templates.with_raw_response.create(
            template_id="x",
            channel="email",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome email",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.journeys.templates.with_streaming_response.create(
            template_id="x",
            channel="email",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome email",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.templates.with_raw_response.create(
                template_id="",
                channel="email",
                notification={
                    "brand": {"id": "id"},
                    "content": {
                        "elements": [{}],
                        "version": "2022-01-01",
                    },
                    "name": "Welcome email",
                    "subscription": {"topic_id": "topic_id"},
                    "tags": ["string"],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        template = client.journeys.templates.retrieve(
            notification_id="x",
            template_id="x",
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.journeys.templates.with_raw_response.retrieve(
            notification_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.journeys.templates.with_streaming_response.retrieve(
            notification_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.templates.with_raw_response.retrieve(
                notification_id="x",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            client.journeys.templates.with_raw_response.retrieve(
                notification_id="",
                template_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        template = client.journeys.templates.list(
            template_id="x",
        )
        assert_matches_type(JourneyTemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        template = client.journeys.templates.list(
            template_id="x",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(JourneyTemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.journeys.templates.with_raw_response.list(
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(JourneyTemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.journeys.templates.with_streaming_response.list(
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(JourneyTemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.templates.with_raw_response.list(
                template_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Courier) -> None:
        template = client.journeys.templates.archive(
            notification_id="x",
            template_id="x",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Courier) -> None:
        response = client.journeys.templates.with_raw_response.archive(
            notification_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Courier) -> None:
        with client.journeys.templates.with_streaming_response.archive(
            notification_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.templates.with_raw_response.archive(
                notification_id="x",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            client.journeys.templates.with_raw_response.archive(
                notification_id="",
                template_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_versions(self, client: Courier) -> None:
        template = client.journeys.templates.list_versions(
            notification_id="x",
            template_id="x",
        )
        assert_matches_type(NotificationTemplateVersionListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_versions(self, client: Courier) -> None:
        response = client.journeys.templates.with_raw_response.list_versions(
            notification_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(NotificationTemplateVersionListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_versions(self, client: Courier) -> None:
        with client.journeys.templates.with_streaming_response.list_versions(
            notification_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(NotificationTemplateVersionListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_versions(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.templates.with_raw_response.list_versions(
                notification_id="x",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            client.journeys.templates.with_raw_response.list_versions(
                notification_id="",
                template_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish(self, client: Courier) -> None:
        template = client.journeys.templates.publish(
            notification_id="x",
            template_id="x",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish_with_all_params(self, client: Courier) -> None:
        template = client.journeys.templates.publish(
            notification_id="x",
            template_id="x",
            version="v321669910225",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Courier) -> None:
        response = client.journeys.templates.with_raw_response.publish(
            notification_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Courier) -> None:
        with client.journeys.templates.with_streaming_response.publish(
            notification_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.templates.with_raw_response.publish(
                notification_id="x",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            client.journeys.templates.with_raw_response.publish(
                notification_id="",
                template_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Courier) -> None:
        template = client.journeys.templates.replace(
            notification_id="x",
            template_id="x",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "name",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Courier) -> None:
        template = client.journeys.templates.replace(
            notification_id="x",
            template_id="x",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [
                        {
                            "channels": ["string"],
                            "if": "if",
                            "loop": "loop",
                            "ref": "ref",
                            "type": "text",
                        }
                    ],
                    "version": "2022-01-01",
                    "scope": "default",
                },
                "name": "name",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
            state="state",
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Courier) -> None:
        response = client.journeys.templates.with_raw_response.replace(
            notification_id="x",
            template_id="x",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "name",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Courier) -> None:
        with client.journeys.templates.with_streaming_response.replace(
            notification_id="x",
            template_id="x",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "name",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.templates.with_raw_response.replace(
                notification_id="x",
                template_id="",
                notification={
                    "brand": {"id": "id"},
                    "content": {
                        "elements": [{}],
                        "version": "2022-01-01",
                    },
                    "name": "name",
                    "subscription": {"topic_id": "topic_id"},
                    "tags": ["string"],
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            client.journeys.templates.with_raw_response.replace(
                notification_id="",
                template_id="x",
                notification={
                    "brand": {"id": "id"},
                    "content": {
                        "elements": [{}],
                        "version": "2022-01-01",
                    },
                    "name": "name",
                    "subscription": {"topic_id": "topic_id"},
                    "tags": ["string"],
                },
            )


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.create(
            template_id="x",
            channel="email",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome email",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.create(
            template_id="x",
            channel="email",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [
                        {
                            "channels": ["string"],
                            "if": "if",
                            "loop": "loop",
                            "ref": "ref",
                            "type": "text",
                        }
                    ],
                    "version": "2022-01-01",
                    "scope": "default",
                },
                "name": "Welcome email",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
            provider_key="x",
            state="state",
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.templates.with_raw_response.create(
            template_id="x",
            channel="email",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome email",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.templates.with_streaming_response.create(
            template_id="x",
            channel="email",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome email",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.create(
                template_id="",
                channel="email",
                notification={
                    "brand": {"id": "id"},
                    "content": {
                        "elements": [{}],
                        "version": "2022-01-01",
                    },
                    "name": "Welcome email",
                    "subscription": {"topic_id": "topic_id"},
                    "tags": ["string"],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.retrieve(
            notification_id="x",
            template_id="x",
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.templates.with_raw_response.retrieve(
            notification_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.templates.with_streaming_response.retrieve(
            notification_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.retrieve(
                notification_id="x",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.retrieve(
                notification_id="",
                template_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.list(
            template_id="x",
        )
        assert_matches_type(JourneyTemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.list(
            template_id="x",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(JourneyTemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.templates.with_raw_response.list(
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(JourneyTemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.templates.with_streaming_response.list(
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(JourneyTemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.list(
                template_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.archive(
            notification_id="x",
            template_id="x",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.templates.with_raw_response.archive(
            notification_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.templates.with_streaming_response.archive(
            notification_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.archive(
                notification_id="x",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.archive(
                notification_id="",
                template_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_versions(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.list_versions(
            notification_id="x",
            template_id="x",
        )
        assert_matches_type(NotificationTemplateVersionListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_versions(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.templates.with_raw_response.list_versions(
            notification_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(NotificationTemplateVersionListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_versions(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.templates.with_streaming_response.list_versions(
            notification_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(NotificationTemplateVersionListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_versions(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.list_versions(
                notification_id="x",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.list_versions(
                notification_id="",
                template_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.publish(
            notification_id="x",
            template_id="x",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish_with_all_params(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.publish(
            notification_id="x",
            template_id="x",
            version="v321669910225",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.templates.with_raw_response.publish(
            notification_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.templates.with_streaming_response.publish(
            notification_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.publish(
                notification_id="x",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.publish(
                notification_id="",
                template_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.replace(
            notification_id="x",
            template_id="x",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "name",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncCourier) -> None:
        template = await async_client.journeys.templates.replace(
            notification_id="x",
            template_id="x",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [
                        {
                            "channels": ["string"],
                            "if": "if",
                            "loop": "loop",
                            "ref": "ref",
                            "type": "text",
                        }
                    ],
                    "version": "2022-01-01",
                    "scope": "default",
                },
                "name": "name",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
            state="state",
        )
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.templates.with_raw_response.replace(
            notification_id="x",
            template_id="x",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "name",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.templates.with_streaming_response.replace(
            notification_id="x",
            template_id="x",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "name",
                "subscription": {"topic_id": "topic_id"},
                "tags": ["string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(JourneyTemplateGetResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.replace(
                notification_id="x",
                template_id="",
                notification={
                    "brand": {"id": "id"},
                    "content": {
                        "elements": [{}],
                        "version": "2022-01-01",
                    },
                    "name": "name",
                    "subscription": {"topic_id": "topic_id"},
                    "tags": ["string"],
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `notification_id` but received ''"):
            await async_client.journeys.templates.with_raw_response.replace(
                notification_id="",
                template_id="x",
                notification={
                    "brand": {"id": "id"},
                    "content": {
                        "elements": [{}],
                        "version": "2022-01-01",
                    },
                    "name": "name",
                    "subscription": {"topic_id": "topic_id"},
                    "tags": ["string"],
                },
            )
