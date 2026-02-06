# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    PutTenantTemplateResponse,
    BaseTemplateTenantAssociation,
    PostTenantTemplatePublishResponse,
)
from courier.types.tenants import (
    TemplateListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        template = client.tenants.templates.retrieve(
            template_id="template_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(BaseTemplateTenantAssociation, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.tenants.templates.with_raw_response.retrieve(
            template_id="template_id",
            tenant_id="tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(BaseTemplateTenantAssociation, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.tenants.templates.with_streaming_response.retrieve(
            template_id="template_id",
            tenant_id="tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(BaseTemplateTenantAssociation, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.templates.with_raw_response.retrieve(
                template_id="template_id",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.tenants.templates.with_raw_response.retrieve(
                template_id="",
                tenant_id="tenant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        template = client.tenants.templates.list(
            tenant_id="tenant_id",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        template = client.tenants.templates.list(
            tenant_id="tenant_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.tenants.templates.with_raw_response.list(
            tenant_id="tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.tenants.templates.with_streaming_response.list(
            tenant_id="tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.templates.with_raw_response.list(
                tenant_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish(self, client: Courier) -> None:
        template = client.tenants.templates.publish(
            template_id="template_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(PostTenantTemplatePublishResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_with_all_params(self, client: Courier) -> None:
        template = client.tenants.templates.publish(
            template_id="template_id",
            tenant_id="tenant_id",
            version="version",
        )
        assert_matches_type(PostTenantTemplatePublishResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Courier) -> None:
        response = client.tenants.templates.with_raw_response.publish(
            template_id="template_id",
            tenant_id="tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(PostTenantTemplatePublishResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Courier) -> None:
        with client.tenants.templates.with_streaming_response.publish(
            template_id="template_id",
            tenant_id="tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(PostTenantTemplatePublishResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.templates.with_raw_response.publish(
                template_id="template_id",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.tenants.templates.with_raw_response.publish(
                template_id="",
                tenant_id="tenant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace(self, client: Courier) -> None:
        template = client.tenants.templates.replace(
            template_id="template_id",
            tenant_id="tenant_id",
            template={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        )
        assert_matches_type(PutTenantTemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Courier) -> None:
        template = client.tenants.templates.replace(
            template_id="template_id",
            tenant_id="tenant_id",
            template={
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
                    "version": "version",
                    "brand": "brand",
                },
                "channels": {
                    "foo": {
                        "brand_id": "brand_id",
                        "if": "if",
                        "metadata": {
                            "utm": {
                                "campaign": "campaign",
                                "content": "content",
                                "medium": "medium",
                                "source": "source",
                                "term": "term",
                            }
                        },
                        "override": {"foo": "bar"},
                        "providers": ["string"],
                        "routing_method": "all",
                        "timeouts": {
                            "channel": 0,
                            "provider": 0,
                        },
                    }
                },
                "providers": {
                    "foo": {
                        "if": "if",
                        "metadata": {
                            "utm": {
                                "campaign": "campaign",
                                "content": "content",
                                "medium": "medium",
                                "source": "source",
                                "term": "term",
                            }
                        },
                        "override": {"foo": "bar"},
                        "timeouts": 0,
                    }
                },
                "routing": {
                    "channels": ["string"],
                    "method": "all",
                },
            },
            published=True,
        )
        assert_matches_type(PutTenantTemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Courier) -> None:
        response = client.tenants.templates.with_raw_response.replace(
            template_id="template_id",
            tenant_id="tenant_id",
            template={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(PutTenantTemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Courier) -> None:
        with client.tenants.templates.with_streaming_response.replace(
            template_id="template_id",
            tenant_id="tenant_id",
            template={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(PutTenantTemplateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.templates.with_raw_response.replace(
                template_id="template_id",
                tenant_id="",
                template={
                    "content": {
                        "elements": [{}],
                        "version": "version",
                    }
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.tenants.templates.with_raw_response.replace(
                template_id="",
                tenant_id="tenant_id",
                template={
                    "content": {
                        "elements": [{}],
                        "version": "version",
                    }
                },
            )


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        template = await async_client.tenants.templates.retrieve(
            template_id="template_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(BaseTemplateTenantAssociation, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.tenants.templates.with_raw_response.retrieve(
            template_id="template_id",
            tenant_id="tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(BaseTemplateTenantAssociation, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.tenants.templates.with_streaming_response.retrieve(
            template_id="template_id",
            tenant_id="tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(BaseTemplateTenantAssociation, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.templates.with_raw_response.retrieve(
                template_id="template_id",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.tenants.templates.with_raw_response.retrieve(
                template_id="",
                tenant_id="tenant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        template = await async_client.tenants.templates.list(
            tenant_id="tenant_id",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        template = await async_client.tenants.templates.list(
            tenant_id="tenant_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.tenants.templates.with_raw_response.list(
            tenant_id="tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.tenants.templates.with_streaming_response.list(
            tenant_id="tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.templates.with_raw_response.list(
                tenant_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncCourier) -> None:
        template = await async_client.tenants.templates.publish(
            template_id="template_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(PostTenantTemplatePublishResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_with_all_params(self, async_client: AsyncCourier) -> None:
        template = await async_client.tenants.templates.publish(
            template_id="template_id",
            tenant_id="tenant_id",
            version="version",
        )
        assert_matches_type(PostTenantTemplatePublishResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncCourier) -> None:
        response = await async_client.tenants.templates.with_raw_response.publish(
            template_id="template_id",
            tenant_id="tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(PostTenantTemplatePublishResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncCourier) -> None:
        async with async_client.tenants.templates.with_streaming_response.publish(
            template_id="template_id",
            tenant_id="tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(PostTenantTemplatePublishResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.templates.with_raw_response.publish(
                template_id="template_id",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.tenants.templates.with_raw_response.publish(
                template_id="",
                tenant_id="tenant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncCourier) -> None:
        template = await async_client.tenants.templates.replace(
            template_id="template_id",
            tenant_id="tenant_id",
            template={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        )
        assert_matches_type(PutTenantTemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncCourier) -> None:
        template = await async_client.tenants.templates.replace(
            template_id="template_id",
            tenant_id="tenant_id",
            template={
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
                    "version": "version",
                    "brand": "brand",
                },
                "channels": {
                    "foo": {
                        "brand_id": "brand_id",
                        "if": "if",
                        "metadata": {
                            "utm": {
                                "campaign": "campaign",
                                "content": "content",
                                "medium": "medium",
                                "source": "source",
                                "term": "term",
                            }
                        },
                        "override": {"foo": "bar"},
                        "providers": ["string"],
                        "routing_method": "all",
                        "timeouts": {
                            "channel": 0,
                            "provider": 0,
                        },
                    }
                },
                "providers": {
                    "foo": {
                        "if": "if",
                        "metadata": {
                            "utm": {
                                "campaign": "campaign",
                                "content": "content",
                                "medium": "medium",
                                "source": "source",
                                "term": "term",
                            }
                        },
                        "override": {"foo": "bar"},
                        "timeouts": 0,
                    }
                },
                "routing": {
                    "channels": ["string"],
                    "method": "all",
                },
            },
            published=True,
        )
        assert_matches_type(PutTenantTemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCourier) -> None:
        response = await async_client.tenants.templates.with_raw_response.replace(
            template_id="template_id",
            tenant_id="tenant_id",
            template={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(PutTenantTemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCourier) -> None:
        async with async_client.tenants.templates.with_streaming_response.replace(
            template_id="template_id",
            tenant_id="tenant_id",
            template={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(PutTenantTemplateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.templates.with_raw_response.replace(
                template_id="template_id",
                tenant_id="",
                template={
                    "content": {
                        "elements": [{}],
                        "version": "version",
                    }
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.tenants.templates.with_raw_response.replace(
                template_id="",
                tenant_id="tenant_id",
                template={
                    "content": {
                        "elements": [{}],
                        "version": "version",
                    }
                },
            )
