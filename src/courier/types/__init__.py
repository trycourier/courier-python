# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared, tenants, notification_list_response
from .. import _compat
from .shared import (
    Utm as Utm,
    Logo as Logo,
    Rule as Rule,
    Brand as Brand,
    Check as Check,
    Icons as Icons,
    Filter as Filter,
    Paging as Paging,
    Tenant as Tenant,
    Audience as Audience,
    Alignment as Alignment,
    BaseCheck as BaseCheck,
    EmailHead as EmailHead,
    Recipient as Recipient,
    TextStyle as TextStyle,
    UserToken as UserToken,
    AuditEvent as AuditEvent,
    Preference as Preference,
    BrandColors as BrandColors,
    EmailFooter as EmailFooter,
    EmailHeader as EmailHeader,
    BrandSnippet as BrandSnippet,
    FilterConfig as FilterConfig,
    BrandSettings as BrandSettings,
    BrandSnippets as BrandSnippets,
    BrandTemplate as BrandTemplate,
    ElementalNode as ElementalNode,
    UserRecipient as UserRecipient,
    MessageContext as MessageContext,
    MessageDetails as MessageDetails,
    MessageRouting as MessageRouting,
    TopicPreference as TopicPreference,
    ElementalContent as ElementalContent,
    PreferenceStatus as PreferenceStatus,
    SubscriptionList as SubscriptionList,
    WidgetBackground as WidgetBackground,
    ChannelPreference as ChannelPreference,
    ElementalBaseNode as ElementalBaseNode,
    TenantAssociation as TenantAssociation,
    BrandSettingsEmail as BrandSettingsEmail,
    BrandSettingsInApp as BrandSettingsInApp,
    DefaultPreferences as DefaultPreferences,
    InboundBulkMessage as InboundBulkMessage,
    ElementalChannelNode as ElementalChannelNode,
    RecipientPreferences as RecipientPreferences,
    SubscriptionTopicNew as SubscriptionTopicNew,
    ChannelClassification as ChannelClassification,
    ElementalContentSugar as ElementalContentSugar,
    MessageRoutingChannel as MessageRoutingChannel,
    InboundBulkMessageUser as InboundBulkMessageUser,
    NotificationGetContent as NotificationGetContent,
    AutomationInvokeResponse as AutomationInvokeResponse,
    ElementalMetaNodeWithType as ElementalMetaNodeWithType,
    ElementalTextNodeWithType as ElementalTextNodeWithType,
    PutSubscriptionsRecipient as PutSubscriptionsRecipient,
    ElementalImageNodeWithType as ElementalImageNodeWithType,
    ElementalQuoteNodeWithType as ElementalQuoteNodeWithType,
    ElementalActionNodeWithType as ElementalActionNodeWithType,
    ElementalChannelNodeWithType as ElementalChannelNodeWithType,
    ElementalDividerNodeWithType as ElementalDividerNodeWithType,
    BaseTemplateTenantAssociation as BaseTemplateTenantAssociation,
    NotificationPreferenceDetails as NotificationPreferenceDetails,
)
from .list_list_params import ListListParams as ListListParams
from .brand_list_params import BrandListParams as BrandListParams
from .list_list_response import ListListResponse as ListListResponse
from .list_update_params import ListUpdateParams as ListUpdateParams
from .tenant_list_params import TenantListParams as TenantListParams
from .brand_create_params import BrandCreateParams as BrandCreateParams
from .brand_list_response import BrandListResponse as BrandListResponse
from .brand_update_params import BrandUpdateParams as BrandUpdateParams
from .message_list_params import MessageListParams as MessageListParams
from .send_message_params import SendMessageParams as SendMessageParams
from .audience_list_params import AudienceListParams as AudienceListParams
from .tenant_list_response import TenantListResponse as TenantListResponse
from .tenant_update_params import TenantUpdateParams as TenantUpdateParams
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
from .audit_event_list_params import AuditEventListParams as AuditEventListParams
from .auth_issue_token_params import AuthIssueTokenParams as AuthIssueTokenParams
from .profile_create_response import ProfileCreateResponse as ProfileCreateResponse
from .audience_update_response import AudienceUpdateResponse as AudienceUpdateResponse
from .bulk_create_job_response import BulkCreateJobResponse as BulkCreateJobResponse
from .bulk_list_users_response import BulkListUsersResponse as BulkListUsersResponse
from .message_content_response import MessageContentResponse as MessageContentResponse
from .message_history_response import MessageHistoryResponse as MessageHistoryResponse
from .notification_list_params import NotificationListParams as NotificationListParams
from .profile_replace_response import ProfileReplaceResponse as ProfileReplaceResponse
from .tenant_list_users_params import TenantListUsersParams as TenantListUsersParams
from .audit_event_list_response import AuditEventListResponse as AuditEventListResponse
from .auth_issue_token_response import AuthIssueTokenResponse as AuthIssueTokenResponse
from .message_retrieve_response import MessageRetrieveResponse as MessageRetrieveResponse
from .profile_retrieve_response import ProfileRetrieveResponse as ProfileRetrieveResponse
from .translation_update_params import TranslationUpdateParams as TranslationUpdateParams
from .bulk_retrieve_job_response import BulkRetrieveJobResponse as BulkRetrieveJobResponse
from .inbound_track_event_params import InboundTrackEventParams as InboundTrackEventParams
from .notification_list_response import NotificationListResponse as NotificationListResponse
from .tenant_list_users_response import TenantListUsersResponse as TenantListUsersResponse
from .audience_list_members_params import AudienceListMembersParams as AudienceListMembersParams
from .inbound_track_event_response import InboundTrackEventResponse as InboundTrackEventResponse
from .translation_retrieve_response import TranslationRetrieveResponse as TranslationRetrieveResponse
from .audience_list_members_response import AudienceListMembersResponse as AudienceListMembersResponse

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
