# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared, tenants, notification_list_response
from .. import _compat
from .logo import Logo as Logo
from .brand import Brand as Brand
from .check import Check as Check
from .icons import Icons as Icons
from .filter import Filter as Filter
from .shared import (
    Utm as Utm,
    Rule as Rule,
    Paging as Paging,
    Alignment as Alignment,
    Recipient as Recipient,
    TextStyle as TextStyle,
    Preference as Preference,
    ElementalNode as ElementalNode,
    UserRecipient as UserRecipient,
    MessageContext as MessageContext,
    MessageRouting as MessageRouting,
    ElementalContent as ElementalContent,
    PreferenceStatus as PreferenceStatus,
    ChannelPreference as ChannelPreference,
    ElementalBaseNode as ElementalBaseNode,
    ElementalChannelNode as ElementalChannelNode,
    RecipientPreferences as RecipientPreferences,
    ChannelClassification as ChannelClassification,
    ElementalContentSugar as ElementalContentSugar,
    MessageRoutingChannel as MessageRoutingChannel,
    ElementalMetaNodeWithType as ElementalMetaNodeWithType,
    ElementalTextNodeWithType as ElementalTextNodeWithType,
    ElementalImageNodeWithType as ElementalImageNodeWithType,
    ElementalQuoteNodeWithType as ElementalQuoteNodeWithType,
    ElementalActionNodeWithType as ElementalActionNodeWithType,
    ElementalChannelNodeWithType as ElementalChannelNodeWithType,
    ElementalDividerNodeWithType as ElementalDividerNodeWithType,
    NotificationPreferenceDetails as NotificationPreferenceDetails,
)
from .tenant import Tenant as Tenant
from .audience import Audience as Audience
from .base_check import BaseCheck as BaseCheck
from .email_head import EmailHead as EmailHead
from .logo_param import LogoParam as LogoParam
from .audit_event import AuditEvent as AuditEvent
from .icons_param import IconsParam as IconsParam
from .brand_colors import BrandColors as BrandColors
from .email_footer import EmailFooter as EmailFooter
from .email_header import EmailHeader as EmailHeader
from .filter_param import FilterParam as FilterParam
from .brand_snippet import BrandSnippet as BrandSnippet
from .brand_settings import BrandSettings as BrandSettings
from .brand_snippets import BrandSnippets as BrandSnippets
from .brand_template import BrandTemplate as BrandTemplate
from .message_details import MessageDetails as MessageDetails
from .base_check_param import BaseCheckParam as BaseCheckParam
from .email_head_param import EmailHeadParam as EmailHeadParam
from .list_list_params import ListListParams as ListListParams
from .brand_list_params import BrandListParams as BrandListParams
from .subscription_list import SubscriptionList as SubscriptionList
from .widget_background import WidgetBackground as WidgetBackground
from .brand_colors_param import BrandColorsParam as BrandColorsParam
from .email_footer_param import EmailFooterParam as EmailFooterParam
from .email_header_param import EmailHeaderParam as EmailHeaderParam
from .list_list_response import ListListResponse as ListListResponse
from .list_update_params import ListUpdateParams as ListUpdateParams
from .tenant_association import TenantAssociation as TenantAssociation
from .tenant_list_params import TenantListParams as TenantListParams
from .brand_create_params import BrandCreateParams as BrandCreateParams
from .brand_list_response import BrandListResponse as BrandListResponse
from .brand_snippet_param import BrandSnippetParam as BrandSnippetParam
from .brand_update_params import BrandUpdateParams as BrandUpdateParams
from .default_preferences import DefaultPreferences as DefaultPreferences
from .message_list_params import MessageListParams as MessageListParams
from .send_message_params import SendMessageParams as SendMessageParams
from .audience_list_params import AudienceListParams as AudienceListParams
from .brand_settings_email import BrandSettingsEmail as BrandSettingsEmail
from .brand_settings_param import BrandSettingsParam as BrandSettingsParam
from .brand_snippets_param import BrandSnippetsParam as BrandSnippetsParam
from .brand_template_param import BrandTemplateParam as BrandTemplateParam
from .inbound_bulk_message import InboundBulkMessage as InboundBulkMessage
from .tenant_list_response import TenantListResponse as TenantListResponse
from .tenant_update_params import TenantUpdateParams as TenantUpdateParams
from .brand_settings_in_app import BrandSettingsInApp as BrandSettingsInApp
from .bulk_add_users_params import BulkAddUsersParams as BulkAddUsersParams
from .message_list_response import MessageListResponse as MessageListResponse
from .profile_create_params import ProfileCreateParams as ProfileCreateParams
from .profile_update_params import ProfileUpdateParams as ProfileUpdateParams
from .send_message_response import SendMessageResponse as SendMessageResponse
from .audience_list_response import AudienceListResponse as AudienceListResponse
from .audience_update_params import AudienceUpdateParams as AudienceUpdateParams
from .bulk_create_job_params import BulkCreateJobParams as BulkCreateJobParams
from .bulk_list_users_params import BulkListUsersParams as BulkListUsersParams
from .message_history_params import MessageHistoryParams as MessageHistoryParams
from .profile_replace_params import ProfileReplaceParams as ProfileReplaceParams
from .subscription_topic_new import SubscriptionTopicNew as SubscriptionTopicNew
from .audit_event_list_params import AuditEventListParams as AuditEventListParams
from .auth_issue_token_params import AuthIssueTokenParams as AuthIssueTokenParams
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
from .tenant_association_param import TenantAssociationParam as TenantAssociationParam
from .tenant_list_users_params import TenantListUsersParams as TenantListUsersParams
from .audit_event_list_response import AuditEventListResponse as AuditEventListResponse
from .auth_issue_token_response import AuthIssueTokenResponse as AuthIssueTokenResponse
from .default_preferences_param import DefaultPreferencesParam as DefaultPreferencesParam
from .inbound_bulk_message_user import InboundBulkMessageUser as InboundBulkMessageUser
from .message_retrieve_response import MessageRetrieveResponse as MessageRetrieveResponse
from .profile_retrieve_response import ProfileRetrieveResponse as ProfileRetrieveResponse
from .translation_update_params import TranslationUpdateParams as TranslationUpdateParams
from .automation_invoke_response import AutomationInvokeResponse as AutomationInvokeResponse
from .brand_settings_email_param import BrandSettingsEmailParam as BrandSettingsEmailParam
from .bulk_retrieve_job_response import BulkRetrieveJobResponse as BulkRetrieveJobResponse
from .inbound_bulk_message_param import InboundBulkMessageParam as InboundBulkMessageParam
from .inbound_track_event_params import InboundTrackEventParams as InboundTrackEventParams
from .notification_list_response import NotificationListResponse as NotificationListResponse
from .tenant_list_users_response import TenantListUsersResponse as TenantListUsersResponse
from .brand_settings_in_app_param import BrandSettingsInAppParam as BrandSettingsInAppParam
from .audience_list_members_params import AudienceListMembersParams as AudienceListMembersParams
from .inbound_track_event_response import InboundTrackEventResponse as InboundTrackEventResponse
from .subscription_topic_new_param import SubscriptionTopicNewParam as SubscriptionTopicNewParam
from .translation_retrieve_response import TranslationRetrieveResponse as TranslationRetrieveResponse
from .audience_list_members_response import AudienceListMembersResponse as AudienceListMembersResponse
from .inbound_bulk_message_user_param import InboundBulkMessageUserParam as InboundBulkMessageUserParam
from .base_template_tenant_association import BaseTemplateTenantAssociation as BaseTemplateTenantAssociation
from .put_subscriptions_recipient_param import PutSubscriptionsRecipientParam as PutSubscriptionsRecipientParam
from .subscribe_to_lists_request_item_param import SubscribeToListsRequestItemParam as SubscribeToListsRequestItemParam

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    notification_list_response.NotificationListResponse.update_forward_refs()  # type: ignore
    tenants.template_list_response.TemplateListResponse.update_forward_refs()  # type: ignore
    shared.message_routing.MessageRouting.update_forward_refs()  # type: ignore
else:
    notification_list_response.NotificationListResponse.model_rebuild(_parent_namespace_depth=0)
    tenants.template_list_response.TemplateListResponse.model_rebuild(_parent_namespace_depth=0)
    shared.message_routing.MessageRouting.model_rebuild(_parent_namespace_depth=0)
