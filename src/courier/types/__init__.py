# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import (
    shared,
    tenants,
    audience,
    journey_response,
    audience_list_response,
    element_with_checksums,
    audience_update_response,
    notification_list_response,
    routing_strategy_get_response,
    notification_content_get_response,
)
from .. import _compat
from .logo import Logo as Logo
from .brand import Brand as Brand
from .check import Check as Check
from .icons import Icons as Icons
from .shared import (
    Utm as Utm,
    Expo as Expo,
    Rule as Rule,
    Slack as Slack,
    Token as Token,
    Paging as Paging,
    Channel as Channel,
    Discord as Discord,
    MsTeams as MsTeams,
    Intercom as Intercom,
    Metadata as Metadata,
    Timeouts as Timeouts,
    Alignment as Alignment,
    Pagerduty as Pagerduty,
    TextStyle as TextStyle,
    DeviceType as DeviceType,
    ListFilter as ListFilter,
    Preference as Preference,
    UserProfile as UserProfile,
    FilterConfig as FilterConfig,
    ElementalNode as ElementalNode,
    ListRecipient as ListRecipient,
    SendToChannel as SendToChannel,
    UserRecipient as UserRecipient,
    WebhookMethod as WebhookMethod,
    AirshipProfile as AirshipProfile,
    AudienceFilter as AudienceFilter,
    MessageContext as MessageContext,
    MessageRouting as MessageRouting,
    MultipleTokens as MultipleTokens,
    SlackRecipient as SlackRecipient,
    WebhookProfile as WebhookProfile,
    ChannelMetadata as ChannelMetadata,
    MessageChannels as MessageChannels,
    WebhookAuthMode as WebhookAuthMode,
    ElementalContent as ElementalContent,
    MessageProviders as MessageProviders,
    MsTeamsRecipient as MsTeamsRecipient,
    PreferenceStatus as PreferenceStatus,
    SendToSlackEmail as SendToSlackEmail,
    WebhookRecipient as WebhookRecipient,
    AudienceRecipient as AudienceRecipient,
    ChannelPreference as ChannelPreference,
    ElementalBaseNode as ElementalBaseNode,
    IntercomRecipient as IntercomRecipient,
    SendDirectMessage as SendDirectMessage,
    SendToSlackUserID as SendToSlackUserID,
    PagerdutyRecipient as PagerdutyRecipient,
    SendToMsTeamsEmail as SendToMsTeamsEmail,
    SendToSlackChannel as SendToSlackChannel,
    WebhookProfileType as WebhookProfileType,
    SendToMsTeamsUserID as SendToMsTeamsUserID,
    SlackBaseProperties as SlackBaseProperties,
    AudienceFilterConfig as AudienceFilterConfig,
    ElementalChannelNode as ElementalChannelNode,
    ListPatternRecipient as ListPatternRecipient,
    MessageProvidersType as MessageProvidersType,
    RecipientPreferences as RecipientPreferences,
    ChannelClassification as ChannelClassification,
    ElementalContentSugar as ElementalContentSugar,
    MessageRoutingChannel as MessageRoutingChannel,
    MsTeamsBaseProperties as MsTeamsBaseProperties,
    WebhookAuthentication as WebhookAuthentication,
    AirshipProfileAudience as AirshipProfileAudience,
    SendToMsTeamsChannelID as SendToMsTeamsChannelID,
    SendToMsTeamsChannelName as SendToMsTeamsChannelName,
    UserProfileFirebaseToken as UserProfileFirebaseToken,
    ElementalHTMLNodeWithType as ElementalHTMLNodeWithType,
    ElementalMetaNodeWithType as ElementalMetaNodeWithType,
    ElementalTextNodeWithType as ElementalTextNodeWithType,
    ElementalImageNodeWithType as ElementalImageNodeWithType,
    ElementalQuoteNodeWithType as ElementalQuoteNodeWithType,
    ElementalActionNodeWithType as ElementalActionNodeWithType,
    SendToMsTeamsConversationID as SendToMsTeamsConversationID,
    ElementalChannelNodeWithType as ElementalChannelNodeWithType,
    ElementalDividerNodeWithType as ElementalDividerNodeWithType,
    NotificationPreferenceDetails as NotificationPreferenceDetails,
)
from .tenant import Tenant as Tenant
from .journey import Journey as Journey
from .audience import Audience as Audience
from .provider import Provider as Provider
from .base_check import BaseCheck as BaseCheck
from .email_head import EmailHead as EmailHead
from .logo_param import LogoParam as LogoParam
from .audit_event import AuditEvent as AuditEvent
from .icons_param import IconsParam as IconsParam
from .brand_colors import BrandColors as BrandColors
from .email_footer import EmailFooter as EmailFooter
from .email_header import EmailHeader as EmailHeader
from .journey_node import JourneyNode as JourneyNode
from .version_node import VersionNode as VersionNode
from .brand_snippet import BrandSnippet as BrandSnippet
from .journey_state import JourneyState as JourneyState
from .brand_settings import BrandSettings as BrandSettings
from .brand_snippets import BrandSnippets as BrandSnippets
from .brand_template import BrandTemplate as BrandTemplate
from .digest_category import DigestCategory as DigestCategory
from .digest_instance import DigestInstance as DigestInstance
from .journey_ai_node import JourneyAINode as JourneyAINode
from .message_details import MessageDetails as MessageDetails
from .base_check_param import BaseCheckParam as BaseCheckParam
from .email_head_param import EmailHeadParam as EmailHeadParam
from .journey_response import JourneyResponse as JourneyResponse
from .list_list_params import ListListParams as ListListParams
from .brand_list_params import BrandListParams as BrandListParams
from .journey_exit_node import JourneyExitNode as JourneyExitNode
from .journey_send_node import JourneySendNode as JourneySendNode
from .subscription_list import SubscriptionList as SubscriptionList
from .widget_background import WidgetBackground as WidgetBackground
from .brand_colors_param import BrandColorsParam as BrandColorsParam
from .email_footer_param import EmailFooterParam as EmailFooterParam
from .email_header_param import EmailHeaderParam as EmailHeaderParam
from .journey_experiment import JourneyExperiment as JourneyExperiment
from .journey_node_param import JourneyNodeParam as JourneyNodeParam
from .list_list_response import ListListResponse as ListListResponse
from .list_update_params import ListUpdateParams as ListUpdateParams
from .tenant_association import TenantAssociation as TenantAssociation
from .tenant_list_params import TenantListParams as TenantListParams
from .automation_template import AutomationTemplate as AutomationTemplate
from .brand_create_params import BrandCreateParams as BrandCreateParams
from .brand_list_response import BrandListResponse as BrandListResponse
from .brand_snippet_param import BrandSnippetParam as BrandSnippetParam
from .brand_update_params import BrandUpdateParams as BrandUpdateParams
from .default_preferences import DefaultPreferences as DefaultPreferences
from .journey_list_params import JourneyListParams as JourneyListParams
from .message_list_params import MessageListParams as MessageListParams
from .send_message_params import SendMessageParams as SendMessageParams
from .audience_list_params import AudienceListParams as AudienceListParams
from .brand_settings_email import BrandSettingsEmail as BrandSettingsEmail
from .brand_settings_param import BrandSettingsParam as BrandSettingsParam
from .brand_snippets_param import BrandSnippetsParam as BrandSnippetsParam
from .brand_template_param import BrandTemplateParam as BrandTemplateParam
from .inbound_bulk_message import InboundBulkMessage as InboundBulkMessage
from .journey_version_item import JourneyVersionItem as JourneyVersionItem
from .provider_list_params import ProviderListParams as ProviderListParams
from .tenant_list_response import TenantListResponse as TenantListResponse
from .tenant_update_params import TenantUpdateParams as TenantUpdateParams
from .brand_settings_in_app import BrandSettingsInApp as BrandSettingsInApp
from .bulk_add_users_params import BulkAddUsersParams as BulkAddUsersParams
from .journey_ai_node_param import JourneyAINodeParam as JourneyAINodeParam
from .journey_cancel_params import JourneyCancelParams as JourneyCancelParams
from .journey_create_params import JourneyCreateParams as JourneyCreateParams
from .journey_invoke_params import JourneyInvokeParams as JourneyInvokeParams
from .message_list_response import MessageListResponse as MessageListResponse
from .profile_create_params import ProfileCreateParams as ProfileCreateParams
from .profile_update_params import ProfileUpdateParams as ProfileUpdateParams
from .send_message_response import SendMessageResponse as SendMessageResponse
from .audience_list_response import AudienceListResponse as AudienceListResponse
from .audience_update_params import AudienceUpdateParams as AudienceUpdateParams
from .automation_list_params import AutomationListParams as AutomationListParams
from .bulk_create_job_params import BulkCreateJobParams as BulkCreateJobParams
from .bulk_list_users_params import BulkListUsersParams as BulkListUsersParams
from .element_with_checksums import ElementWithChecksums as ElementWithChecksums
from .journey_condition_atom import JourneyConditionAtom as JourneyConditionAtom
from .journey_merge_strategy import JourneyMergeStrategy as JourneyMergeStrategy
from .journey_publish_params import JourneyPublishParams as JourneyPublishParams
from .journey_replace_params import JourneyReplaceParams as JourneyReplaceParams
from .journeys_list_response import JourneysListResponse as JourneysListResponse
from .message_history_params import MessageHistoryParams as MessageHistoryParams
from .profile_replace_params import ProfileReplaceParams as ProfileReplaceParams
from .provider_create_params import ProviderCreateParams as ProviderCreateParams
from .provider_list_response import ProviderListResponse as ProviderListResponse
from .provider_update_params import ProviderUpdateParams as ProviderUpdateParams
from .subscription_topic_new import SubscriptionTopicNew as SubscriptionTopicNew
from .audit_event_list_params import AuditEventListParams as AuditEventListParams
from .auth_issue_token_params import AuthIssueTokenParams as AuthIssueTokenParams
from .cancel_journey_response import CancelJourneyResponse as CancelJourneyResponse
from .journey_condition_group import JourneyConditionGroup as JourneyConditionGroup
from .journey_exit_node_param import JourneyExitNodeParam as JourneyExitNodeParam
from .journey_retrieve_params import JourneyRetrieveParams as JourneyRetrieveParams
from .journey_send_node_param import JourneySendNodeParam as JourneySendNodeParam
from .message_resend_response import MessageResendResponse as MessageResendResponse
from .profile_create_response import ProfileCreateResponse as ProfileCreateResponse
from .providers_catalog_entry import ProvidersCatalogEntry as ProvidersCatalogEntry
from .widget_background_param import WidgetBackgroundParam as WidgetBackgroundParam
from .audience_update_response import AudienceUpdateResponse as AudienceUpdateResponse
from .bulk_create_job_response import BulkCreateJobResponse as BulkCreateJobResponse
from .bulk_list_users_response import BulkListUsersResponse as BulkListUsersResponse
from .journey_conditions_field import JourneyConditionsField as JourneyConditionsField
from .journey_delay_until_node import JourneyDelayUntilNode as JourneyDelayUntilNode
from .journey_experiment_param import JourneyExperimentParam as JourneyExperimentParam
from .journey_template_summary import JourneyTemplateSummary as JourneyTemplateSummary
from .journeys_invoke_response import JourneysInvokeResponse as JourneysInvokeResponse
from .message_content_response import MessageContentResponse as MessageContentResponse
from .message_history_response import MessageHistoryResponse as MessageHistoryResponse
from .notification_get_content import NotificationGetContent as NotificationGetContent
from .notification_list_params import NotificationListParams as NotificationListParams
from .profile_replace_response import ProfileReplaceResponse as ProfileReplaceResponse
from .routing_strategy_summary import RoutingStrategySummary as RoutingStrategySummary
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
from .journey_experiment_variant import JourneyExperimentVariant as JourneyExperimentVariant
from .notification_create_params import NotificationCreateParams as NotificationCreateParams
from .notification_list_response import NotificationListResponse as NotificationListResponse
from .tenant_list_users_response import TenantListUsersResponse as TenantListUsersResponse
from .brand_settings_in_app_param import BrandSettingsInAppParam as BrandSettingsInAppParam
from .journey_delay_duration_node import JourneyDelayDurationNode as JourneyDelayDurationNode
from .journey_fetch_post_put_node import JourneyFetchPostPutNode as JourneyFetchPostPutNode
from .notification_publish_params import NotificationPublishParams as NotificationPublishParams
from .notification_replace_params import NotificationReplaceParams as NotificationReplaceParams
from .notification_template_state import NotificationTemplateState as NotificationTemplateState
from .tenant_template_input_param import TenantTemplateInputParam as TenantTemplateInputParam
from .audience_list_members_params import AudienceListMembersParams as AudienceListMembersParams
from .cancel_journey_request_param import CancelJourneyRequestParam as CancelJourneyRequestParam
from .inbound_track_event_response import InboundTrackEventResponse as InboundTrackEventResponse
from .journey_condition_atom_param import JourneyConditionAtomParam as JourneyConditionAtomParam
from .journey_segment_trigger_node import JourneySegmentTriggerNode as JourneySegmentTriggerNode
from .journey_throttle_static_node import JourneyThrottleStaticNode as JourneyThrottleStaticNode
from .notification_retrieve_params import NotificationRetrieveParams as NotificationRetrieveParams
from .publish_preferences_response import PublishPreferencesResponse as PublishPreferencesResponse
from .put_tenant_template_response import PutTenantTemplateResponse as PutTenantTemplateResponse
from .routing_strategy_list_params import RoutingStrategyListParams as RoutingStrategyListParams
from .subscription_topic_new_param import SubscriptionTopicNewParam as SubscriptionTopicNewParam
from .digest_instance_list_response import DigestInstanceListResponse as DigestInstanceListResponse
from .journey_condition_group_param import JourneyConditionGroupParam as JourneyConditionGroupParam
from .journey_fetch_get_delete_node import JourneyFetchGetDeleteNode as JourneyFetchGetDeleteNode
from .journey_template_get_response import JourneyTemplateGetResponse as JourneyTemplateGetResponse
from .journey_throttle_dynamic_node import JourneyThrottleDynamicNode as JourneyThrottleDynamicNode
from .notification_template_payload import NotificationTemplatePayload as NotificationTemplatePayload
from .notification_template_summary import NotificationTemplateSummary as NotificationTemplateSummary
from .routing_strategy_get_response import RoutingStrategyGetResponse as RoutingStrategyGetResponse
from .translation_retrieve_response import TranslationRetrieveResponse as TranslationRetrieveResponse
from .audience_list_members_response import AudienceListMembersResponse as AudienceListMembersResponse
from .journey_condition_nested_group import JourneyConditionNestedGroup as JourneyConditionNestedGroup
from .journey_conditions_field_param import JourneyConditionsFieldParam as JourneyConditionsFieldParam
from .journey_delay_until_node_param import JourneyDelayUntilNodeParam as JourneyDelayUntilNodeParam
from .journey_template_list_response import JourneyTemplateListResponse as JourneyTemplateListResponse
from .journey_versions_list_response import JourneyVersionsListResponse as JourneyVersionsListResponse
from .notification_put_locale_params import NotificationPutLocaleParams as NotificationPutLocaleParams
from .notification_template_response import NotificationTemplateResponse as NotificationTemplateResponse
from .routing_strategy_create_params import RoutingStrategyCreateParams as RoutingStrategyCreateParams
from .routing_strategy_list_response import RoutingStrategyListResponse as RoutingStrategyListResponse
from .inbound_bulk_message_user_param import InboundBulkMessageUserParam as InboundBulkMessageUserParam
from .journey_api_invoke_trigger_node import JourneyAPIInvokeTriggerNode as JourneyAPIInvokeTriggerNode
from .notification_put_content_params import NotificationPutContentParams as NotificationPutContentParams
from .notification_put_element_params import NotificationPutElementParams as NotificationPutElementParams
from .routing_strategy_replace_params import RoutingStrategyReplaceParams as RoutingStrategyReplaceParams
from .base_template_tenant_association import BaseTemplateTenantAssociation as BaseTemplateTenantAssociation
from .journey_experiment_variant_param import JourneyExperimentVariantParam as JourneyExperimentVariantParam
from .automation_template_list_response import AutomationTemplateListResponse as AutomationTemplateListResponse
from .journey_delay_duration_node_param import JourneyDelayDurationNodeParam as JourneyDelayDurationNodeParam
from .journey_fetch_post_put_node_param import JourneyFetchPostPutNodeParam as JourneyFetchPostPutNodeParam
from .notification_content_get_response import NotificationContentGetResponse as NotificationContentGetResponse
from .notification_list_versions_params import NotificationListVersionsParams as NotificationListVersionsParams
from .put_subscriptions_recipient_param import PutSubscriptionsRecipientParam as PutSubscriptionsRecipientParam
from .workspace_preference_get_response import WorkspacePreferenceGetResponse as WorkspacePreferenceGetResponse
from .journey_segment_trigger_node_param import JourneySegmentTriggerNodeParam as JourneySegmentTriggerNodeParam
from .journey_throttle_static_node_param import JourneyThrottleStaticNodeParam as JourneyThrottleStaticNodeParam
from .workspace_preference_create_params import WorkspacePreferenceCreateParams as WorkspacePreferenceCreateParams
from .workspace_preference_list_response import WorkspacePreferenceListResponse as WorkspacePreferenceListResponse
from .journey_fetch_get_delete_node_param import JourneyFetchGetDeleteNodeParam as JourneyFetchGetDeleteNodeParam
from .journey_throttle_dynamic_node_param import JourneyThrottleDynamicNodeParam as JourneyThrottleDynamicNodeParam
from .notification_template_payload_param import NotificationTemplatePayloadParam as NotificationTemplatePayloadParam
from .workspace_preference_publish_params import WorkspacePreferencePublishParams as WorkspacePreferencePublishParams
from .workspace_preference_replace_params import WorkspacePreferenceReplaceParams as WorkspacePreferenceReplaceParams
from .journey_condition_nested_group_param import JourneyConditionNestedGroupParam as JourneyConditionNestedGroupParam
from .notification_retrieve_content_params import NotificationRetrieveContentParams as NotificationRetrieveContentParams
from .associated_notification_list_response import (
    AssociatedNotificationListResponse as AssociatedNotificationListResponse,
)
from .journey_api_invoke_trigger_node_param import JourneyAPIInvokeTriggerNodeParam as JourneyAPIInvokeTriggerNodeParam
from .post_tenant_template_publish_response import (
    PostTenantTemplatePublishResponse as PostTenantTemplatePublishResponse,
)
from .subscribe_to_lists_request_item_param import SubscribeToListsRequestItemParam as SubscribeToListsRequestItemParam
from .notification_content_mutation_response import (
    NotificationContentMutationResponse as NotificationContentMutationResponse,
)
from .notification_retrieve_content_response import (
    NotificationRetrieveContentResponse as NotificationRetrieveContentResponse,
)
from .workspace_preference_topic_get_response import (
    WorkspacePreferenceTopicGetResponse as WorkspacePreferenceTopicGetResponse,
)
from .workspace_preference_topic_list_response import (
    WorkspacePreferenceTopicListResponse as WorkspacePreferenceTopicListResponse,
)
from .routing_strategy_list_notifications_params import (
    RoutingStrategyListNotificationsParams as RoutingStrategyListNotificationsParams,
)
from .notification_template_version_list_response import (
    NotificationTemplateVersionListResponse as NotificationTemplateVersionListResponse,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    audience.Audience.update_forward_refs()  # type: ignore
    audience_update_response.AudienceUpdateResponse.update_forward_refs()  # type: ignore
    audience_list_response.AudienceListResponse.update_forward_refs()  # type: ignore
    journey_response.JourneyResponse.update_forward_refs()  # type: ignore
    element_with_checksums.ElementWithChecksums.update_forward_refs()  # type: ignore
    notification_content_get_response.NotificationContentGetResponse.update_forward_refs()  # type: ignore
    notification_list_response.NotificationListResponse.update_forward_refs()  # type: ignore
    routing_strategy_get_response.RoutingStrategyGetResponse.update_forward_refs()  # type: ignore
    tenants.template_list_response.TemplateListResponse.update_forward_refs()  # type: ignore
    shared.audience_filter_config.AudienceFilterConfig.update_forward_refs()  # type: ignore
    shared.filter_config.FilterConfig.update_forward_refs()  # type: ignore
    shared.message_routing.MessageRouting.update_forward_refs()  # type: ignore
else:
    audience.Audience.model_rebuild(_parent_namespace_depth=0)
    audience_update_response.AudienceUpdateResponse.model_rebuild(_parent_namespace_depth=0)
    audience_list_response.AudienceListResponse.model_rebuild(_parent_namespace_depth=0)
    journey_response.JourneyResponse.model_rebuild(_parent_namespace_depth=0)
    element_with_checksums.ElementWithChecksums.model_rebuild(_parent_namespace_depth=0)
    notification_content_get_response.NotificationContentGetResponse.model_rebuild(_parent_namespace_depth=0)
    notification_list_response.NotificationListResponse.model_rebuild(_parent_namespace_depth=0)
    routing_strategy_get_response.RoutingStrategyGetResponse.model_rebuild(_parent_namespace_depth=0)
    tenants.template_list_response.TemplateListResponse.model_rebuild(_parent_namespace_depth=0)
    shared.audience_filter_config.AudienceFilterConfig.model_rebuild(_parent_namespace_depth=0)
    shared.filter_config.FilterConfig.model_rebuild(_parent_namespace_depth=0)
    shared.message_routing.MessageRouting.model_rebuild(_parent_namespace_depth=0)
