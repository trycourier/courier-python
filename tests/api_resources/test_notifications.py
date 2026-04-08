# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    NotificationListResponse,
    NotificationTemplateGetResponse,
    NotificationContentMutationResponse,
    NotificationRetrieveContentResponse,
    NotificationTemplateMutationResponse,
    NotificationTemplateVersionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        notification = client.notifications.create(
            notification={
                "brand": {"id": "brand_abc"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome Email",
                "routing": {"strategy_id": "rs_123"},
                "subscription": {"topic_id": "marketing"},
                "tags": ["onboarding", "welcome"],
            },
        )
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.create(
            notification={
                "brand": {"id": "brand_abc"},
                "content": {
                    "elements": [{"type": "channel"}],
                    "version": "2022-01-01",
                },
                "name": "Welcome Email",
                "routing": {"strategy_id": "rs_123"},
                "subscription": {"topic_id": "marketing"},
                "tags": ["onboarding", "welcome"],
            },
            state="DRAFT",
        )
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.create(
            notification={
                "brand": {"id": "brand_abc"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome Email",
                "routing": {"strategy_id": "rs_123"},
                "subscription": {"topic_id": "marketing"},
                "tags": ["onboarding", "welcome"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.create(
            notification={
                "brand": {"id": "brand_abc"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome Email",
                "routing": {"strategy_id": "rs_123"},
                "subscription": {"topic_id": "marketing"},
                "tags": ["onboarding", "welcome"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        notification = client.notifications.retrieve(
            id="id",
        )
        assert_matches_type(NotificationTemplateGetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.retrieve(
            id="id",
            version="version",
        )
        assert_matches_type(NotificationTemplateGetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationTemplateGetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationTemplateGetResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        notification = client.notifications.list()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.list(
            cursor="cursor",
            event_id="event_id",
            notes=True,
        )
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationListResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Courier) -> None:
        notification = client.notifications.archive(
            "id",
        )
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.archive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.archive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_versions(self, client: Courier) -> None:
        notification = client.notifications.list_versions(
            id="id",
        )
        assert_matches_type(NotificationTemplateVersionListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_versions_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.list_versions(
            id="id",
            cursor="cursor",
            limit=10,
        )
        assert_matches_type(NotificationTemplateVersionListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_versions(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.list_versions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationTemplateVersionListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_versions(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.list_versions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationTemplateVersionListResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_versions(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.with_raw_response.list_versions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish(self, client: Courier) -> None:
        notification = client.notifications.publish(
            id="id",
        )
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.publish(
            id="id",
            version="v321669910225",
        )
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.publish(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.publish(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.with_raw_response.publish(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_put_content(self, client: Courier) -> None:
        notification = client.notifications.put_content(
            id="id",
            content={"elements": [{}]},
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_put_content_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.put_content(
            id="id",
            content={
                "elements": [{"type": "channel"}],
                "version": "2022-01-01",
            },
            state="DRAFT",
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_put_content(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.put_content(
            id="id",
            content={"elements": [{}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_put_content(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.put_content(
            id="id",
            content={"elements": [{}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_put_content(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.with_raw_response.put_content(
                id="",
                content={"elements": [{}]},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_put_element(self, client: Courier) -> None:
        notification = client.notifications.put_element(
            element_id="elementId",
            id="id",
            type="text",
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_put_element_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.put_element(
            element_id="elementId",
            id="id",
            type="text",
            channels=["string"],
            data={"content": "bar"},
            if_="if",
            loop="loop",
            ref="ref",
            state="DRAFT",
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_put_element(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.put_element(
            element_id="elementId",
            id="id",
            type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_put_element(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.put_element(
            element_id="elementId",
            id="id",
            type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_put_element(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.with_raw_response.put_element(
                element_id="elementId",
                id="",
                type="text",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `element_id` but received ''"):
            client.notifications.with_raw_response.put_element(
                element_id="",
                id="id",
                type="text",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_put_locale(self, client: Courier) -> None:
        notification = client.notifications.put_locale(
            locale_id="localeId",
            id="id",
            elements=[{"id": "elem_1"}, {"id": "elem_2"}],
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_put_locale_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.put_locale(
            locale_id="localeId",
            id="id",
            elements=[{"id": "elem_1"}, {"id": "elem_2"}],
            state="DRAFT",
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_put_locale(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.put_locale(
            locale_id="localeId",
            id="id",
            elements=[{"id": "elem_1"}, {"id": "elem_2"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_put_locale(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.put_locale(
            locale_id="localeId",
            id="id",
            elements=[{"id": "elem_1"}, {"id": "elem_2"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_put_locale(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.with_raw_response.put_locale(
                locale_id="localeId",
                id="",
                elements=[{"id": "elem_1"}, {"id": "elem_2"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale_id` but received ''"):
            client.notifications.with_raw_response.put_locale(
                locale_id="",
                id="id",
                elements=[{"id": "elem_1"}, {"id": "elem_2"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Courier) -> None:
        notification = client.notifications.replace(
            id="id",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Updated Name",
                "routing": {"strategy_id": "strategy_id"},
                "subscription": {"topic_id": "topic_id"},
                "tags": ["updated"],
            },
        )
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.replace(
            id="id",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{"type": "channel"}],
                    "version": "2022-01-01",
                },
                "name": "Updated Name",
                "routing": {"strategy_id": "strategy_id"},
                "subscription": {"topic_id": "topic_id"},
                "tags": ["updated"],
            },
            state="PUBLISHED",
        )
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.replace(
            id="id",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Updated Name",
                "routing": {"strategy_id": "strategy_id"},
                "subscription": {"topic_id": "topic_id"},
                "tags": ["updated"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.replace(
            id="id",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Updated Name",
                "routing": {"strategy_id": "strategy_id"},
                "subscription": {"topic_id": "topic_id"},
                "tags": ["updated"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.with_raw_response.replace(
                id="",
                notification={
                    "brand": {"id": "id"},
                    "content": {
                        "elements": [{}],
                        "version": "2022-01-01",
                    },
                    "name": "Updated Name",
                    "routing": {"strategy_id": "strategy_id"},
                    "subscription": {"topic_id": "topic_id"},
                    "tags": ["updated"],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_content(self, client: Courier) -> None:
        notification = client.notifications.retrieve_content(
            id="id",
        )
        assert_matches_type(NotificationRetrieveContentResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_content_with_all_params(self, client: Courier) -> None:
        notification = client.notifications.retrieve_content(
            id="id",
            version="version",
        )
        assert_matches_type(NotificationRetrieveContentResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_content(self, client: Courier) -> None:
        response = client.notifications.with_raw_response.retrieve_content(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationRetrieveContentResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_content(self, client: Courier) -> None:
        with client.notifications.with_streaming_response.retrieve_content(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationRetrieveContentResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_content(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.with_raw_response.retrieve_content(
                id="",
            )


class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.create(
            notification={
                "brand": {"id": "brand_abc"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome Email",
                "routing": {"strategy_id": "rs_123"},
                "subscription": {"topic_id": "marketing"},
                "tags": ["onboarding", "welcome"],
            },
        )
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.create(
            notification={
                "brand": {"id": "brand_abc"},
                "content": {
                    "elements": [{"type": "channel"}],
                    "version": "2022-01-01",
                },
                "name": "Welcome Email",
                "routing": {"strategy_id": "rs_123"},
                "subscription": {"topic_id": "marketing"},
                "tags": ["onboarding", "welcome"],
            },
            state="DRAFT",
        )
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.create(
            notification={
                "brand": {"id": "brand_abc"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome Email",
                "routing": {"strategy_id": "rs_123"},
                "subscription": {"topic_id": "marketing"},
                "tags": ["onboarding", "welcome"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.create(
            notification={
                "brand": {"id": "brand_abc"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Welcome Email",
                "routing": {"strategy_id": "rs_123"},
                "subscription": {"topic_id": "marketing"},
                "tags": ["onboarding", "welcome"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.retrieve(
            id="id",
        )
        assert_matches_type(NotificationTemplateGetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.retrieve(
            id="id",
            version="version",
        )
        assert_matches_type(NotificationTemplateGetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationTemplateGetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationTemplateGetResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.list()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.list(
            cursor="cursor",
            event_id="event_id",
            notes=True,
        )
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationListResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.archive(
            "id",
        )
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.archive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.archive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_versions(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.list_versions(
            id="id",
        )
        assert_matches_type(NotificationTemplateVersionListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_versions_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.list_versions(
            id="id",
            cursor="cursor",
            limit=10,
        )
        assert_matches_type(NotificationTemplateVersionListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_versions(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.list_versions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationTemplateVersionListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_versions(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.list_versions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationTemplateVersionListResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_versions(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.with_raw_response.list_versions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.publish(
            id="id",
        )
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.publish(
            id="id",
            version="v321669910225",
        )
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.publish(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert notification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.publish(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.with_raw_response.publish(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_put_content(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.put_content(
            id="id",
            content={"elements": [{}]},
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_put_content_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.put_content(
            id="id",
            content={
                "elements": [{"type": "channel"}],
                "version": "2022-01-01",
            },
            state="DRAFT",
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_put_content(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.put_content(
            id="id",
            content={"elements": [{}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_put_content(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.put_content(
            id="id",
            content={"elements": [{}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_put_content(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.with_raw_response.put_content(
                id="",
                content={"elements": [{}]},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_put_element(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.put_element(
            element_id="elementId",
            id="id",
            type="text",
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_put_element_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.put_element(
            element_id="elementId",
            id="id",
            type="text",
            channels=["string"],
            data={"content": "bar"},
            if_="if",
            loop="loop",
            ref="ref",
            state="DRAFT",
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_put_element(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.put_element(
            element_id="elementId",
            id="id",
            type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_put_element(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.put_element(
            element_id="elementId",
            id="id",
            type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_put_element(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.with_raw_response.put_element(
                element_id="elementId",
                id="",
                type="text",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `element_id` but received ''"):
            await async_client.notifications.with_raw_response.put_element(
                element_id="",
                id="id",
                type="text",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_put_locale(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.put_locale(
            locale_id="localeId",
            id="id",
            elements=[{"id": "elem_1"}, {"id": "elem_2"}],
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_put_locale_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.put_locale(
            locale_id="localeId",
            id="id",
            elements=[{"id": "elem_1"}, {"id": "elem_2"}],
            state="DRAFT",
        )
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_put_locale(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.put_locale(
            locale_id="localeId",
            id="id",
            elements=[{"id": "elem_1"}, {"id": "elem_2"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_put_locale(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.put_locale(
            locale_id="localeId",
            id="id",
            elements=[{"id": "elem_1"}, {"id": "elem_2"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationContentMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_put_locale(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.with_raw_response.put_locale(
                locale_id="localeId",
                id="",
                elements=[{"id": "elem_1"}, {"id": "elem_2"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locale_id` but received ''"):
            await async_client.notifications.with_raw_response.put_locale(
                locale_id="",
                id="id",
                elements=[{"id": "elem_1"}, {"id": "elem_2"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.replace(
            id="id",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Updated Name",
                "routing": {"strategy_id": "strategy_id"},
                "subscription": {"topic_id": "topic_id"},
                "tags": ["updated"],
            },
        )
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.replace(
            id="id",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{"type": "channel"}],
                    "version": "2022-01-01",
                },
                "name": "Updated Name",
                "routing": {"strategy_id": "strategy_id"},
                "subscription": {"topic_id": "topic_id"},
                "tags": ["updated"],
            },
            state="PUBLISHED",
        )
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.replace(
            id="id",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Updated Name",
                "routing": {"strategy_id": "strategy_id"},
                "subscription": {"topic_id": "topic_id"},
                "tags": ["updated"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.replace(
            id="id",
            notification={
                "brand": {"id": "id"},
                "content": {
                    "elements": [{}],
                    "version": "2022-01-01",
                },
                "name": "Updated Name",
                "routing": {"strategy_id": "strategy_id"},
                "subscription": {"topic_id": "topic_id"},
                "tags": ["updated"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationTemplateMutationResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.with_raw_response.replace(
                id="",
                notification={
                    "brand": {"id": "id"},
                    "content": {
                        "elements": [{}],
                        "version": "2022-01-01",
                    },
                    "name": "Updated Name",
                    "routing": {"strategy_id": "strategy_id"},
                    "subscription": {"topic_id": "topic_id"},
                    "tags": ["updated"],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_content(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.retrieve_content(
            id="id",
        )
        assert_matches_type(NotificationRetrieveContentResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_content_with_all_params(self, async_client: AsyncCourier) -> None:
        notification = await async_client.notifications.retrieve_content(
            id="id",
            version="version",
        )
        assert_matches_type(NotificationRetrieveContentResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_content(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.with_raw_response.retrieve_content(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationRetrieveContentResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_content(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.with_streaming_response.retrieve_content(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationRetrieveContentResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_content(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.with_raw_response.retrieve_content(
                id="",
            )
