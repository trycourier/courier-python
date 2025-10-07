# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import (
    tenants,
    audience,
    message_routing,
    nested_filter_config,
    audience_list_response,
    audience_update_response,
    notification_list_response,
)
from .. import _compat
from .list import List as List
from .logo import Logo as Logo
from .brand import Brand as Brand
from .icons import Icons as Icons
from .filter import Filter as Filter
from .paging import Paging as Paging
from .shared import Rule as Rule, Preference as Preference, ChannelPreference as ChannelPreference
from .tenant import Tenant as Tenant
from .content import Content as Content
from .audience import Audience as Audience
from .utm_param import UtmParam as UtmParam
from .email_head import EmailHead as EmailHead
from .logo_param import LogoParam as LogoParam
from .audit_event import AuditEvent as AuditEvent
from .icons_param import IconsParam as IconsParam
from .brand_colors import BrandColors as BrandColors
from .email_footer import EmailFooter as EmailFooter
from .email_header import EmailHeader as EmailHeader
from .filter_param import FilterParam as FilterParam
from .brand_snippet import BrandSnippet as BrandSnippet
from .content_param import ContentParam as ContentParam
from .filter_config import FilterConfig as FilterConfig
from .brand_settings import BrandSettings as BrandSettings
from .brand_snippets import BrandSnippets as BrandSnippets
from .brand_template import BrandTemplate as BrandTemplate
from .user_recipient import UserRecipient as UserRecipient
from .message_context import MessageContext as MessageContext
from .message_details import MessageDetails as MessageDetails
from .message_routing import MessageRouting as MessageRouting
from .recipient_param import RecipientParam as RecipientParam
from .email_head_param import EmailHeadParam as EmailHeadParam
from .list_list_params import ListListParams as ListListParams
from .brand_list_params import BrandListParams as BrandListParams
from .widget_background import WidgetBackground as WidgetBackground
from .brand_colors_param import BrandColorsParam as BrandColorsParam
from .email_footer_param import EmailFooterParam as EmailFooterParam
from .email_header_param import EmailHeaderParam as EmailHeaderParam
from .list_list_response import ListListResponse as ListListResponse
from .list_update_params import ListUpdateParams as ListUpdateParams
from .tenant_list_params import TenantListParams as TenantListParams
from .brand_create_params import BrandCreateParams as BrandCreateParams
from .brand_list_response import BrandListResponse as BrandListResponse
from .brand_snippet_param import BrandSnippetParam as BrandSnippetParam
from .brand_update_params import BrandUpdateParams as BrandUpdateParams
from .default_preferences import DefaultPreferences as DefaultPreferences
from .filter_config_param import FilterConfigParam as FilterConfigParam
from .message_list_params import MessageListParams as MessageListParams
from .audience_list_params import AudienceListParams as AudienceListParams
from .brand_settings_email import BrandSettingsEmail as BrandSettingsEmail
from .brand_settings_param import BrandSettingsParam as BrandSettingsParam
from .brand_snippets_param import BrandSnippetsParam as BrandSnippetsParam
from .brand_template_param import BrandTemplateParam as BrandTemplateParam
from .inbound_bulk_message import InboundBulkMessage as InboundBulkMessage
from .nested_filter_config import NestedFilterConfig as NestedFilterConfig
from .tenant_list_response import TenantListResponse as TenantListResponse
from .tenant_update_params import TenantUpdateParams as TenantUpdateParams
from .user_recipient_param import UserRecipientParam as UserRecipientParam
from .brand_settings_in_app import BrandSettingsInApp as BrandSettingsInApp
from .bulk_add_users_params import BulkAddUsersParams as BulkAddUsersParams
from .message_context_param import MessageContextParam as MessageContextParam
from .message_list_response import MessageListResponse as MessageListResponse
from .message_routing_param import MessageRoutingParam as MessageRoutingParam
from .profile_create_params import ProfileCreateParams as ProfileCreateParams
from .profile_update_params import ProfileUpdateParams as ProfileUpdateParams
from .audience_list_response import AudienceListResponse as AudienceListResponse
from .audience_update_params import AudienceUpdateParams as AudienceUpdateParams
from .bulk_create_job_params import BulkCreateJobParams as BulkCreateJobParams
from .bulk_list_users_params import BulkListUsersParams as BulkListUsersParams
from .message_history_params import MessageHistoryParams as MessageHistoryParams
from .profile_replace_params import ProfileReplaceParams as ProfileReplaceParams
from .audit_event_list_params import AuditEventListParams as AuditEventListParams
from .auth_issue_token_params import AuthIssueTokenParams as AuthIssueTokenParams
from .message_routing_channel import MessageRoutingChannel as MessageRoutingChannel
from .profile_create_response import ProfileCreateResponse as ProfileCreateResponse
from .widget_background_param import WidgetBackgroundParam as WidgetBackgroundParam
from .audience_update_response import AudienceUpdateResponse as AudienceUpdateResponse
from .bulk_create_job_response import BulkCreateJobResponse as BulkCreateJobResponse
from .bulk_list_users_response import BulkListUsersResponse as BulkListUsersResponse
from .message_content_response import MessageContentResponse as MessageContentResponse
from .message_history_response import MessageHistoryResponse as MessageHistoryResponse
from .notification_get_content import NotificationGetContent as NotificationGetContent
from .notification_list_params import NotificationListParams as NotificationListParams
from .profile_replace_response import ProfileReplaceResponse as ProfileReplaceResponse
from .send_send_message_params import SendSendMessageParams as SendSendMessageParams
from .tenant_list_users_params import TenantListUsersParams as TenantListUsersParams
from .audit_event_list_response import AuditEventListResponse as AuditEventListResponse
from .auth_issue_token_response import AuthIssueTokenResponse as AuthIssueTokenResponse
from .default_preferences_param import DefaultPreferencesParam as DefaultPreferencesParam
from .inbound_bulk_message_user import InboundBulkMessageUser as InboundBulkMessageUser
from .message_retrieve_response import MessageRetrieveResponse as MessageRetrieveResponse
from .profile_retrieve_response import ProfileRetrieveResponse as ProfileRetrieveResponse
from .translation_update_params import TranslationUpdateParams as TranslationUpdateParams
from .brand_settings_email_param import BrandSettingsEmailParam as BrandSettingsEmailParam
from .bulk_retrieve_job_response import BulkRetrieveJobResponse as BulkRetrieveJobResponse
from .inbound_bulk_message_param import InboundBulkMessageParam as InboundBulkMessageParam
from .inbound_track_event_params import InboundTrackEventParams as InboundTrackEventParams
from .nested_filter_config_param import NestedFilterConfigParam as NestedFilterConfigParam
from .notification_list_response import NotificationListResponse as NotificationListResponse
from .send_send_message_response import SendSendMessageResponse as SendSendMessageResponse
from .tenant_list_users_response import TenantListUsersResponse as TenantListUsersResponse
from .brand_settings_in_app_param import BrandSettingsInAppParam as BrandSettingsInAppParam
from .audience_list_members_params import AudienceListMembersParams as AudienceListMembersParams
from .inbound_track_event_response import InboundTrackEventResponse as InboundTrackEventResponse
from .message_routing_channel_param import MessageRoutingChannelParam as MessageRoutingChannelParam
from .translation_retrieve_response import TranslationRetrieveResponse as TranslationRetrieveResponse
from .audience_list_members_response import AudienceListMembersResponse as AudienceListMembersResponse
from .inbound_bulk_message_user_param import InboundBulkMessageUserParam as InboundBulkMessageUserParam

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    audience.Audience.update_forward_refs()  # type: ignore
    nested_filter_config.NestedFilterConfig.update_forward_refs()  # type: ignore
    audience_update_response.AudienceUpdateResponse.update_forward_refs()  # type: ignore
    audience_list_response.AudienceListResponse.update_forward_refs()  # type: ignore
    message_routing.MessageRouting.update_forward_refs()  # type: ignore
    notification_list_response.NotificationListResponse.update_forward_refs()  # type: ignore
    tenants.template_list_response.TemplateListResponse.update_forward_refs()  # type: ignore
else:
    audience.Audience.model_rebuild(_parent_namespace_depth=0)
    nested_filter_config.NestedFilterConfig.model_rebuild(_parent_namespace_depth=0)
    audience_update_response.AudienceUpdateResponse.model_rebuild(_parent_namespace_depth=0)
    audience_list_response.AudienceListResponse.model_rebuild(_parent_namespace_depth=0)
    message_routing.MessageRouting.model_rebuild(_parent_namespace_depth=0)
    notification_list_response.NotificationListResponse.model_rebuild(_parent_namespace_depth=0)
    tenants.template_list_response.TemplateListResponse.model_rebuild(_parent_namespace_depth=0)
